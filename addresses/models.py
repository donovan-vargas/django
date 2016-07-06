# coding=utf-8
from __future__ import unicode_literals


from django.contrib.auth.models import User
from django.contrib.gis.db import models
from django.db import models


# Create your models here.
class StatesCatalog(models.Model):
    """Catalogo de Estados"""
    state = models.CharField("Estado", max_length=60)

    class Meta(object):
        verbose_name_plural = "Catalogo de estados"

    def __unicode__(self):
        return self.state


class CitiesCatalog(models.Model):
    """Catalogo de Ciudades"""
    city = models.CharField("Ciudad", max_length=60)

    class Meta(object):
        verbose_name_plural = "Catalogo de ciudades"

    def __unicode__(self):
        return self.city


class SuburbCatalog(models.Model):
    """Catalogo de Colonias"""
    suburb = models.CharField("Colonia", max_length=100)
    code = models.CharField("Codigo", max_length=10)

    class Meta(object):
        verbose_name_plural = "Catalogo de colonias"

    def __str__(self):
        return self.suburb


class PostalCodeCatalog(models.Model):
    """Catalogo de Códigos postales"""
    postal_code = models.CharField("Código postal", max_length=10)

    class Meta(object):
        verbose_name_plural = "Catalogo de CP"

    def __unicode__(self):
        return self.postal_code


class Addresses(models.Model):
    # Modelo para el registro de direcciones por usuario
    user = models.ForeignKey(User)
    state = models.OneToOneField(StatesCatalog)
    city = models.OneToOneField(CitiesCatalog)
    suburb = models.OneToOneField(SuburbCatalog)
    street = models.CharField("Calle", max_length=150)
    crossing_x = models.CharField("Cruzamiento", max_length=150, null=True, blank=True)
    crossing_y = models.CharField("Cruzamiento", max_length=150, null=True, blank=True)
    postal_code = models.OneToOneField(PostalCodeCatalog)
    number = models.CharField("Numero", max_length=30)

    class Meta(object):
        verbose_name_plural = "Direcciones"

    def __str__(self):
        return self.user.username
