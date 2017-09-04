from django.shortcuts import render, get_object_or_404, redirect
from products_module.models import Produit
from crm_module.models import Contact
from .models import Commande
from .forms import FormulaireCommmande

def liste_commande(request):
    commandes = Commande.objects.all()
    total = commandes.count()
    tab = {}
    for i in range(total):
        client_id = Commande.objects.values_list('client', flat=True)[i]
        client = Contact.objects.filter(id=client_id).values_list('nom', flat=True)[0]
        tab[i] = client
    return render(request, 'commandes/liste_commandes.html', {'commandes' : commandes, 'tab': tab})

def creer_commande(request):
    if request.method != "POST":
        form = FormulaireCommmande()
        return render(request, 'commandes/creer_commande.html', {"form" : form})
    else:
        form = FormulaireCommmande(request.POST)
        if form.is_valid():
            commandes = Commande(client="2", produit="9", depot=False)
            commandes.save()
            return redirect(liste_commande)

def supprimer_commande(request, id):
    Commande.objects.filter(id=id).delete()
    return redirect(liste_commande)