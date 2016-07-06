# coding=utf-8
from __future__ import unicode_literals

from django.conf import settings
from django.contrib.gis.db import models
from django.db import models
<<<<<<< HEAD
=======


# Create your models here.


class StatesCatalog(models.Model):
    """Catalogo de Estados"""
    state = models.CharField(max_length=60)

    def __unicode__(self):
        return self.state


class CitiesCatalog(models.Model):
    """Catalogo de Ciudades"""
    city = models.CharField(max_length=60)

    def __unicode__(self):
        return self.city


class SuburbCatalog(models.Model):
    """Catalogo de Colonias"""
    suburb = models.CharField(max_length=100)
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.suburb


class PostalCodeCatalog(models.Model):
    """Catalogo de Códigos postales"""
    postal_code = models.CharField(max_length=10)

    def __unicode__(self):
        return self.postal_code
>>>>>>> f5e9ad2b2513f9a876289f5ac2623a93702833c3


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    photo = models.ImageField("Foto", upload_to='profiles', blank=True, null=True)
    telephone = models.CharField("Teléfono", max_length=15, blank=True, null=True)
    services = models.IntegerField("Servicios solicitados", null=True, blank=True)
    score = models.FloatField("Calificacion", null=True, blank=True)
    reg_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)


    class Meta(object):
        verbose_name_plural = "Perfil de usuarios"

    def __str__(self):
        return self.user.username
