from django import forms
from .models import Contact

class FormulaireContact(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('nom', 'adresse', 'code_postal', 'localite', 'pays', 'telephone', 'email', 'num_tva' , 'type_client', 'statut_client', 'interraction')