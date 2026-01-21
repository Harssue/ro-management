from django.contrib import admin
from .models import Customer, ServiceRecord
# Register your models here.
class ServiceLine(admin.TabularInline):
    model = ServiceRecord
    extra = 1

class CustomerAd(admin.ModelAdmin):
    inlines = [ServiceLine]
    search_fields = ['id', 'name', 'phone']

admin.site.register(Customer, CustomerAd)