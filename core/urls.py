from django.urls import path
from .views import home, search_customer, AddCustomer, EditCustomer, DeleteCustomer, AddService, register, index, next1, AddSparePart, next2, spare_master, logout

urlpatterns = [
    path('', index, name='index'),
    path('logged_out/', logout, name='logged_out'),
    # path('purchase-spare/', PurchaseSpare.as_view(), name='purchase-spare'),
    path('next1/next2/spare-master/', spare_master, name='spare-master'),
    path('next1/next2/add-spare/', AddSparePart.as_view(), name='add-spare'),
    path('next1/', next1, name='next1'),
    path('next1/next2/', next2, name='next2'),
    path('register/', register, name='register'),
    path('next1/home/', home, name='cust_data'),
    path('next1/home/search_customer/', search_customer, name='search_customer'),
    path('next1/home/add-cust/', AddCustomer.as_view(), name='add-cust'),
    path('next1/next2/add-serv/', AddService.as_view(), name='add-serv'),
    path('next1/home/edit-cust/<int:id>/',EditCustomer.as_view(), name='edit-cust'),
    path('delete-cust/',DeleteCustomer.as_view(), name='delete-cust'),
]