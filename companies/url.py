# coding=utf-8
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^registro/$', views.register_company_view, name='companies.registro'),
]
