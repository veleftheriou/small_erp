from django import forms
from .models import Produit


class FormulaireProduits(forms.ModelForm):
    class Meta:
        model = Produit
        fields = ('nom', 'description', 'origine', 'ean', 'numero_lot', 'prix_achat', 'prix_revente_gros', 'prix_revente_particuliers', )