# coding=utf-8
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User


# Create your models here.
class ActivityCatalog(models.Model):
    activity = models.CharField(max_length=40)
    relation = models.CharField(max_length=200)
    description = models.CharField(max_length=180)


class JobCatalog(models.Model):
    JUNIOR = 'JR'
    SEMISENIOR = 'SS'
    SENIOR = 'SR'
    CATEGORY_CHOICE = (
        (JUNIOR, 'Junior'),
        (SEMISENIOR, 'Semisenior'),
        (SENIOR, 'Senior'),
    )

    job = models.CharField(max_length=40)
    description = models.CharField(max_length=200)
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICE, default=JUNIOR)


class DepartmentsCatalog(models.Model):
    department = models.CharField(max_length=30)
    activities = models.CharField(max_length=120)


class CompanyUser(models.Model):
    company = models.OneToOneField(settings.AUTH_USER_MODEL)
    logo = models.ImageField(upload_to='profiles', blank=True, null=True)
    activity = models.ForeignKey(ActivityCatalog)
    state = models.ForeignKey('accounts.StatesCatalog')
    city = models.ForeignKey('accounts.CitiesCatalog')
    suburb = models.ForeignKey('accounts.SuburbCatalog')
    street = models.CharField(max_length=150)
    crossing_x = models.CharField(max_length=150, null=True, blank=True)
    crossing_y = models.CharField(max_length=150, null=True, blank=True)
    postal_code = models.ForeignKey('accounts.PostalCodeCatalog')
    number = models.CharField(max_length=30)
    RFC = models.CharField(max_length=13)
    telephone = models.CharField(max_length=15, blank=True, null=True)
    type = models.CharField(default='company', editable=False)


class CompanyEmployees(models.Model):
    ANY = 'AN'
    ELEMENTARY = 'EL'
    HIGH_SCOOL = 'HS'
    COLLEGE = 'CL'
    SCHOOL_CHOICE = (
        (ANY, 'Ninguno'),
        (ELEMENTARY, 'Primaria'),
        (HIGH_SCOOL, 'Secundaria'),
        (COLLEGE, 'Universidad'),
    )

    MALE = 'M'
    FEMALE = 'F'
    SEX_CHOICE = (
        (MALE, 'Hombre'),
        (FEMALE, 'Mujer')
    )

    SINGLE = 'SG'
    MARRIED = 'MR'
    FREE_UNION = 'FU'
    DIVORCED = 'DV'
    WIDOWER = 'WW'
    CIVIL_STATUS_CHOICE = (
        (SINGLE, 'Soltero'),
        (MARRIED, 'Casado'),
        (FREE_UNION, 'Union libre'),
        (DIVORCED, 'Divorciado'),
        (WIDOWER, 'Viudo'),
    )

    employee = models.OneToOneField(settings.AUTH_USER_MODEL)
    birthdate = models.DateField()
    imss = models.IntegerField(validators=[MaxValueValidator(999999999999999), ])
    telephone = models.CharField(max_length=15, blank=True, null=True)
    salary = models.DecimalField(max_digits=6, decimal_places=2)
    job = models.ForeignKey(JobCatalog)
    department = models.ForeignKey(DepartmentsCatalog)
    num_employee = models.IntegerField()
    studies = models.CharField(max_length=2, choices=SCHOOL_CHOICE, default=ANY)
    sex = models.CharField(max_length=1, choices=SEX_CHOICE, default=MALE)
    curp = models.CharField(max_length=18, null=True, blank=True)
    civil_status = models.CharField(max_length=2, choices=CIVIL_STATUS_CHOICE, default=SINGLE)


class ProductCatalog(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    SEX_CHOICE = (
        (MALE, 'Hombre'),
        (FEMALE, 'Mujer')
    )

    company = models.ForeignKey(User)
    slug = models.SlugField(max_length=80)  # etiqueta para url amigables
    product_name = models.CharField(max_length=80)
    patent = models.CharField(max_length=80)  # Marca
    series = models.CharField(max_length=20, null=True, blank=True)
    origin = models.CharField(max_length=20, null=True, blank=True)  # origen
    net = models.DecimalField(max_digits=6, decimal_places=2)  # contenido neto
    measure = models.DecimalField(max_digits=6, decimal_places=2)  # medida
    
