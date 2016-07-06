# coding=utf-8
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator


# Create your models here.
class ProviderCatalog(models.Model):
    name = models.CharField("nombre", max_length=40)
    RFC = models.CharField(max_length=13, blank=True, null=True)
    registry_date = models.DateTimeField("fecha registro", auto_now=True)
    facture_name = models.CharField("Nombre facturación", blank=True, null=True)
    email = models.EmailField("email", blank=True, null=True)
    web = models.CharField("Pagina web", blank=True, null=True)
    telephone = models.CharField("Teléfono", blank=True, null=True, max_length=30)



class ProducerCatalog(models.Model):
    producer = models.CharField("productor", max_length=40)
    country = models.CharField("país", max_length=40)

    class Meta(object):
        verbose_name_plural = 'Catalogo de productores'

    def __str__(self):
        return self.producer


class ProductCatalog(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    SEX_CHOICE = (
        (MALE, 'Hombre'),
        (FEMALE, 'Mujer')
    )

    company = models.ForeignKey(User)
    slug = models.SlugField("etiquetas", max_length=80)  # etiqueta para url amigables
    product_name = models.CharField("nombre del producto", max_length=80)
    patent = models.CharField("marca", max_length=80)  # Marca
    series = models.CharField("serie", max_length=20, null=True, blank=True)
    origin = models.CharField("origen", max_length=20, null=True, blank=True)  # origen
    net = models.DecimalField("contenido", max_digits=6, decimal_places=2)  # contenido neto
    measure = models.DecimalField("medida", max_digits=6, decimal_places=2)  # medida
    barcode = models.IntegerField("código de barras", validators=[MaxValueValidator(999999999999999), ])
    producer = models.ForeignKey(ProducerCatalog)
    provider = models.ForeignKey(ProviderCatalog)

    class Meta(object):
        verbose_name_plural = 'Catalogo de productos'

    def __str__(self):
        return '%s %s' % (self.product_name, self.patent)


class Store(models.Model):
    name = models.CharField("nombre", max_length=40)
    description = models.CharField("descripción", max_length=120, blank=True, null=True)

    class Meta(object):
        verbose_name_plural = 'Almacén'

    def __str__(self):
        return self.name

class Inventory(models.Model):
    store = models.ForeignKey(Store)
    product = models.ForeignKey(ProductCatalog)
    quantity = models.DecimalField("cantidad", max_digits=6, decimal_places=2)
    entry = models.DecimalField("entradas", max_digits=6, decimal_places=2)
    date_entry = models.DateTimeField("Fecha de entrada", auto_now=True)
    user = models.OneToOneField(User)
    out = models.DecimalField("salidas", max_digits=6, decimal_places=2)
