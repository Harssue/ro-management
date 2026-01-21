from django.db import models

# Create your models here.
class Customer(models.Model):
    serial_key = models.IntegerField(max_length=8, unique=True)
    name = models.CharField(max_length=60)
    address = models.TextField()
    phone = models.IntegerField()
    installation_date = models.DateField()

    def __str__(self):
        return f'{self.serial_key} - {self.name}'
    
class SparePart(models.Model):
    serial_number = models.IntegerField(max_length=8, unique=True)
    part_name = models.CharField(max_length=60)
    part_price = models.FloatField()
    opening_qty = models.IntegerField()

    def __str__(self):
        return f'{self.serial_number} - {self.part_name}'

class ServiceRecord(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='service_history')
    service_date = models.DateField()
    parts_used = models.ForeignKey(SparePart, on_delete=models.CASCADE, related_name='parts_used')
    opening_qty = models.IntegerField()

    def __str__(self):
        return f'{self.customer.name} - {self.service_date}'

class PurchaseOrder(models.Model):
    serial_number = models.IntegerField(max_length=8)
    part_name = models.CharField(max_length=60)
    part_price = models.FloatField()
    quantity = models.IntegerField()