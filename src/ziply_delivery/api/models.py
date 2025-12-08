from django.db import models
from client.models import Customer
from company.models import Company

# Create your models here.


class Parcel(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    status = models.CharField(max_length=100)
    barcode = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    update_time = models.DateTimeField(auto_now=True)
    additional_info = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Parcel {self.barcode}"


class InventoryRecord(models.Model):
    parcel = models.OneToOneField(Parcel, on_delete=models.CASCADE)

    stock = models.IntegerField()
    warehouse_location = models.CharField(max_length=200)
    reason_waiting = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Inventory for {self.parcel.barcode}"
