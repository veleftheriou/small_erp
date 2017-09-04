from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^produits/$', views.liste_produits, name='liste_produits'),
    url(r'^produits/creer$', views.creer_produit, name='creer_produit'),
    url(r'^produits/editer/(?P<id>\d+)$', views.editer_produit, name='editer_produit'),
    url(r'^produits/supprimer/(?P<id>\d+)$', views.supprimer_produit, name='supprimer_produit'),
    url(r'^stock/$', views.liste_stock, name="liste_stock")

]