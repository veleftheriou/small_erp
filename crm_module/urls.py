from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^contacts/$', views.liste_contacts, name="liste_contacts"),
    url(r'^contacts/creer/$', views.creer_contact, name="creer_contact"),
    url(r'^contacts/editer/(?P<id>\d+)$', views.editer_contact, name="editer_contact"),
    url(r'^contacts/supprimer/(?P<id>\d+)$', views.supprimer_contact, name="supprimer_contact")

]