# coding=utf-8
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^agregar_direccion/$', views.add_address_view, name='addresses.agregar_direccion'),
    url(r'^editar_direccion/(?P<pk>\d+)/$', views.edit_address_view, name='addresses.editar_direccion'),
]