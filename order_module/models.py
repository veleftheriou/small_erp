from django.db import models
from products_module.models import Produit
from crm_module.models import Contact


class Commande(models.Model):
    date = models.DateField(auto_now_add=True)
    client = models.ForeignKey(Contact)
    produit = models.ManyToManyField(Produit)
    depot = models.BooleanField(default=False)
