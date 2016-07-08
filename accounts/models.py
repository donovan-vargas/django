# coding=utf-8
from __future__ import unicode_literals

from django.conf import settings
from django.contrib.gis.db import models
from django.db import models


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
