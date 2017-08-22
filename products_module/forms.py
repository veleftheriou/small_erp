from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'origin', 'ean', 'package_number', 'buy_price', 'wholesale_price', 'retail_price' )
