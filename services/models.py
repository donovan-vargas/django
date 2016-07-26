# coding=utf-8
from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from products.models import ProductCatalog


class ServicesCatalog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    service = models.CharField("servicio", max_length=60)
    description = models.CharField("descripción", max_length=120, blank=True, null=True)
    domicilie = models.BooleanField("a domicilio", default=False)
    store = models.BooleanField("en sucursal", default=True)
    price = models.DecimalField("precio", max_digits=6, decimal_places=2)


class ProductService(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    service = models.ForeignKey(ServicesCatalog)
    product = models.ManyToManyField(ProductCatalog)
    quantity = models.DecimalField("cantidad", max_digits=6, decimal_places=2)
