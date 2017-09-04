from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^commandes/$', views.liste_commande, name="liste_commandes"),
    url(r'^commandes/creer/$', views.creer_commande, name="creer_commande"),
    url(r'^commandes/supprimer/(?P<id>\d+)$', views.supprimer_commande, name='supprimer_commande'),
]