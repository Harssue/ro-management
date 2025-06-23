from django import forms
from .models import Customer,ServiceHis,AddSpareParts,PurchaseFormModel
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AddCustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['serial_key', "name", 'address', 'phone', 'installation_date']
        widgets = {
            'installation_date':forms.DateInput(attrs={'type':'date'}),
        }

class AddServiceForm(forms.ModelForm):
    class Meta:
        model = ServiceHis
        fields = ['customer', 'service_date', 'parts_used', 'opening_qty']
        widgets = {
            'service_date':forms.DateInput(attrs={'type':'date'}),
        }

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class AddSparePartsForm(forms.ModelForm):
    class Meta:
        model = AddSpareParts
        fields = ['serial_number', 'part_name', 'part_price', 'opening_qty']

class PurchaseSpareForm(forms.ModelForm):
    class Meta:
        model = PurchaseFormModel
        fields = ['serial_number', 'part_name', 'part_price', 'quantity']