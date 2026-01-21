from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.views import View
from .models import Customer, SparePart
from .forms import AddCustomerForm, AddServiceForm, UserRegistrationForm, AddSparePartsForm,PurchaseSpareForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
# Create your views here.

def customer_list(request):
    customer = Customer.objects.all()
    return render(request, 'home.html', {'cust_data': customer})

def search_customer(request):
    context = {}
    if request.method == 'GET':
        id = request.GET.get('id')
        if id:
            customer = get_object_or_404(Customer, id=id)
            context['customer'] = customer
    return render(request, 'search.html', context)

class AddCustomer(View):
    def get(self, request):
        form = AddCustomerForm()
        return render(request, 'add-cust.html', {'form':form})
    
    def post(self, request):
        form = AddCustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
        else:
            return render(request, 'add-cust.html', {'form':form})

class AddService(View):
    def get(self, request):
        form = AddServiceForm()
        return render(request, 'add-serv.html', {'form': form})

    def post(self, request):
        form = AddServiceForm(request.POST)
        if form.is_valid():
            customer = form.cleaned_data['customer']
            service_date = form.cleaned_data['service_date']
            parts_used = form.cleaned_data['parts_used']
            opening_qty = form.cleaned_data['opening_qty']

            existing_part = SparePart.objects.get(id=parts_used.id)
            existing_part.opening_qty -= opening_qty
            existing_part.save()

            form.save()
            return redirect('inventory_list')
        return render(request, 'add-serv.html', {'form': form})

class EditCustomer(View):
    def get(self, request, id):
        customer = Customer.objects.get(pk=id)
        form = AddCustomerForm(instance=customer)
        return render(request, 'edit-cust.html', {'form':form})
    
    def post(self, request, id):
        customer = Customer.objects.get(pk=id)
        form = AddCustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
        else:
            return render(request, 'edit-cust.html', {'form':form})

class DeleteCustomer(View):
    def post(self, request):
        data = request.POST
        id = data.get('id')
        cust_data = Customer.objects.get(id=id)
        cust_data.delete()
        return redirect('customer_list')

def register(request):
    if request.method=='POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
            return redirect ('dashboard')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def index(request):
    return render(request, 'registration/index.html')

def dashboard(request):
    return render(request, 'next1.html')

def operations_menu(request):
    return render(request, 'next2.html')

class AddSparePart(View):
    def get(self, request):
        form = AddSparePartsForm()
        return render(request, 'add-spare.html', {'form':form})
    
    def post(self, request):
        form = AddSparePartsForm(request.POST)
        if form.is_valid():
            serial_number = form.cleaned_data['serial_number']
            part_name = form.cleaned_data['part_name']
            part_price = form.cleaned_data['part_price']
            opening_qty = form.cleaned_data['opening_qty']

            try:
                existing_part = SparePart.objects.get(serial_number=serial_number)
                existing_part.opening_qty += opening_qty
                existing_part.save()
            except SparePart.DoesNotExist:
                form.save()
            return redirect('inventory_list')
        return render(request, 'add-spare.html', {'form':form})

def inventory_list(request):
    spare = SparePart.objects.all()
    return render(request, 'spare-master.html', {'spare_data':spare})

def logout(request):
    return render(request, 'registration/logged_out.html')

# class PurchaseSpare(View):
#     def get(self, request):
#         form = PurchaseSpareForm()
#         return render(request, 'purchase-spare.html', {'form':form})
    
#     def post(self, request):
#         form = PurchaseSpareForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/spare-master')
#         else:
#             return render(request, 'purchase-spare.html', {'form':form})