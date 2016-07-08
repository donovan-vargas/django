# coding=utf-8
from __future__ import unicode_literals

from django.conf import settings
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.db import models


# Create your models here.
class ActivityCatalog(models.Model):
    JUNIOR = 'JR'
    SEMISENIOR = 'SS'
    SENIOR = 'SR'
    CATEGORY_CHOICE = (
        (JUNIOR, 'Junior'),
        (SEMISENIOR, 'Semisenior'),
        (SENIOR, 'Senior'),
    )

    activity = models.CharField("actividad", max_length=40)
    relation = models.CharField("relación", max_length=200)
    description = models.CharField("descripción", max_length=180)

    class Meta(object):
        verbose_name_plural = 'Catalogo de actividades'

    def __str__(self):
        return self.activity


class JobCatalog(models.Model):
    JUNIOR = 'JR'
    SEMISENIOR = 'SS'
    SENIOR = 'SR'
    CATEGORY_CHOICE = (
        (JUNIOR, 'Junior'),
        (SEMISENIOR, 'Semisenior'),
        (SENIOR, 'Senior'),
    )

    job = models.CharField("puesto", max_length=40)
    description = models.CharField("descripción", max_length=200)
    category = models.CharField("categoría", max_length=2, choices=CATEGORY_CHOICE, default=JUNIOR)

    class Meta(object):
        verbose_name_plural = 'Catalogo de puestos'

    def __str__(self):
        return self.job


class DepartmentsCatalog(models.Model):
    department = models.CharField("departamento", max_length=30)
    activities = models.CharField("actividad", max_length=120)

    class Meta(object):
        verbose_name_plural = "Catalogo de departamentos"

    def __str__(self):
        return self.department





class CompanyUser(models.Model):
    company = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name="compañia")
    logo = models.ImageField("logotipo", upload_to='profiles', blank=True, null=True)
    activity = models.ManyToManyField(ActivityCatalog, verbose_name="actividades relacionadas")
    RFC = models.CharField(max_length=13, blank=True, null=True)
    telephone = models.CharField("teléfono", max_length=15, blank=True, null=True)
    ceo = models.CharField("Director", max_length=50, blank=True, null=True)


    class Meta(object):
        verbose_name_plural = "Compañía"

    def __str__(self):
        return '%s %s' % (self.company, self.activity)


class BranchCompany(models.Model):
    branch = models.CharField("sucursal", max_length=40)
    telephone = models.CharField("teléfono", max_length=15, blank=True, null=True)
    manager = models.OneToOneField('CompanyEmployees')

    class Meta(object):
        verbose_name_plural = 'Sucursales'

    def __str__(self):
        return self.branch


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

    employee = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="empleado")
    birthdate = models.DateField("fecha de nacimiento")
    imss = models.IntegerField(validators=[MaxValueValidator(999999999999999), ])
    telephone = models.CharField("teléfono", max_length=15, blank=True, null=True)
    salary = models.DecimalField("salario", max_digits=6, decimal_places=2)
    job = models.OneToOneField(JobCatalog)
    department = models.OneToOneField(DepartmentsCatalog)
    num_employee = models.IntegerField("numero de empleado")
    studies = models.CharField("grado de estudios", max_length=2, choices=SCHOOL_CHOICE, default=ANY)
    sex = models.CharField("sexo", max_length=1, choices=SEX_CHOICE, default=MALE)
    curp = models.CharField(max_length=18, null=True, blank=True)
    civil_status = models.CharField("estado civl", max_length=2, choices=CIVIL_STATUS_CHOICE, default=SINGLE)
    branch = models.OneToOneField(BranchCompany)

    class Meta(object):
        verbose_name_plural = 'Empleados'

    def __str__(self):
        return '%s %s' % (self.employee, self.department)
