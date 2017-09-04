from django import forms
from .models import Commande
from products_module.models import Produit
from crm_module.models import Contact

class FormulaireCommmande(forms.Form):
    produit = forms.ModelChoiceField(queryset=Produit.objects.all().order_by('nom'))
    client = forms.ModelChoiceField(queryset=Contact.objects.all().order_by('nom'))
    quantite = forms.IntegerField(max_value=100)
    depot = forms.BooleanField(help_text="Est-ce un dépot ?", required=False)