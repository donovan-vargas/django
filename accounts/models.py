# coding=utf-8
from __future__ import unicode_literals

from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.gis.db import models
from django.db import models


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


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    photo = models.ImageField(upload_to='profiles', blank=True, null=True)
    telephone = models.CharField(max_length=15, blank=True, null=True)
    services = models.IntegerField(null=True, blank=True)
    score = models.FloatField(null=True, blank=True)
    reg_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    type = models.CharField(default='user', editable=False, max_length=30)

    def __str__(self):
        return self.user.username


class UserAddress(models.Model):
    # Modelo para el registro de direcciones por usuario
    user = models.ForeignKey(User)
    state = models.ForeignKey(StatesCatalog)
    city = models.ForeignKey(CitiesCatalog)
    suburb = models.ForeignKey(SuburbCatalog)
    street = models.CharField(max_length=150)
    crossing_x = models.CharField(max_length=150, null=True, blank=True)
    crossing_y = models.CharField(max_length=150, null=True, blank=True)
    postal_code = models.ForeignKey(PostalCodeCatalog)
    number = models.CharField(max_length=30)

    def __str__(self):
        return self.user.username
