from django.conf.urls import url, include
from django.views.generic import TemplateView
from django.contrib import admin

from products_module import views

urlpatterns = [
	url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^products/$', views.product_list, name='product_list'),
    url(r'^products/create/$', views.product_create, name='product_create'),
    url(r'^products/(?P<pk>\d+)/update/$', views.product_update, name='product_update'),
    url(r'^products/(?P<pk>\d+)/delete/$', views.product_delete, name='product_delete'),
]
