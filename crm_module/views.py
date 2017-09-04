from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact
from .forms import FormulaireContact

# Create your views here.


def liste_contacts(request):
    contacts = Contact.objects.all()
    return render (request, 'crm/liste_contacts.html', {'contacts' : contacts})



def creer_contact(request):
    if request.method != "POST":
        form = FormulaireContact()
        return render (request, 'crm/creer_contact.html', {'form' : form})
    else:
        form = FormulaireContact(request.POST)
        if form.is_valid():
            form.save()
            return redirect(liste_contacts)



def editer_contact(request, id):
    contact = get_object_or_404(Contact, pk=id)
    if request.method != "POST":
        form = FormulaireContact(instance=contact)
        return render(request, 'crm/editer_contact.html', {'form': form})
    else:
        form = FormulaireContact(data=request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect(liste_contacts)



def supprimer_contact(request,id):
    Contact.objects.filter(id=id).delete()
    return redirect(liste_contacts)