from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=160, blank=True)
    origin = models.CharField(max_length=50)
    ean = models.CharField(max_length=13, blank=True)
    package_number = models.CharField(max_length=10, blank=True)
    buy_price = models.DecimalField(max_digits=6, decimal_places=2)
    wholesale_price = models.DecimalField(max_digits=6, decimal_places=2)
    retail_price = models.DecimalField(max_digits=6, decimal_places=2)