from django.urls import path
from .views import (
    index, dashboard, operations_menu, inventory_list, customer_list,
    search_customer, register, logout,
    AddCustomer, EditCustomer, DeleteCustomer, AddService, AddSparePart
)

urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout_view'), # Renamed to avoid name clash with django.contrib.auth.logout but view is custom
    
    path('dashboard/', dashboard, name='dashboard'),
    path('operations/', operations_menu, name='operations_menu'),
    
    # Customer Management
    path('customers/', customer_list, name='customer_list'),
    path('customers/add/', AddCustomer.as_view(), name='add_customer'),
    path('customers/search/', search_customer, name='search_customer'),
    path('customers/edit/<int:id>/', EditCustomer.as_view(), name='edit_customer'),
    path('customers/delete/', DeleteCustomer.as_view(), name='delete_customer'),
    
    # Service & Inventory
    path('service/add/', AddService.as_view(), name='add_service'),
    path('inventory/', inventory_list, name='inventory_list'),
    path('inventory/add/', AddSparePart.as_view(), name='add_spare_part'),
]