from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class Produit(models.Model):
    nom = models.CharField(max_length=80)
    description = models.CharField(max_length=160, blank=True)
    origine = models.CharField(max_length=50)
    ean = models.CharField(max_length=13, blank=True)
    numero_lot = models.CharField(max_length=10, blank=True)
    prix_achat = models.DecimalField(max_digits=6, decimal_places=2)
    prix_revente_gros = models.DecimalField(max_digits=6, decimal_places=2)
    prix_revente_particuliers = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField(max_length=3)


'''
class Stock(models.Model):
    produit = models.OneToOneField(
        Produit,
        on_delete=models.CASCADE,
        primary_key=True
    )
    stock = models.PositiveIntegerField(validators=[MinValueValidator(0)])
'''