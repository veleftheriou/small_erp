from django.shortcuts import render, get_object_or_404, redirect
from .models import Produit
from .forms import FormulaireProduits
# Create your views here.


def liste_produits(request):
    produits = Produit.objects.all()
    return render(request, 'produits/liste_produits.html', {'produits': produits})


def creer_produit(request):
    if request.method != "POST":
        form = FormulaireProduits()
        return render(request, 'produits/creer_produit.html', {"form" : form})
    else:
        form = FormulaireProduits(request.POST)
        if form.is_valid():
            form.save()
            return redirect(liste_produits)


def editer_produit(request, id):
    produit = get_object_or_404(Produit, pk=id)
    if request.method != "POST":
        form = FormulaireProduits(instance=produit)
        return render(request, 'produits/editer_produit.html', {'form' : form})
    else:
        form = FormulaireProduits(data=request.POST, instance=produit)
        if form.is_valid():
            form.save()
            return redirect(liste_produits)


def supprimer_produit(request, id):
        Produit.objects.filter(id=id).delete()
        return redirect(liste_produits)


def liste_stock(request):
    produits = Produit.objects.all()
    return render(request, 'produits/liste_stock.html', {'produits': produits})