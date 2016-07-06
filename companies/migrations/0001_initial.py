# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-04 23:45
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityCatalog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.CharField(max_length=40, verbose_name='actividad')),
                ('relation', models.CharField(max_length=200, verbose_name='relaci\xf3n')),
                ('description', models.CharField(max_length=180, verbose_name='descripci\xf3n')),
            ],
            options={
                'verbose_name_plural': 'Catalogo de actividades',
            },
        ),
        migrations.CreateModel(
            name='BranchCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.CharField(max_length=40, verbose_name='sucursal')),
                ('telephone', models.CharField(blank=True, max_length=15, null=True, verbose_name='tel\xe9fono')),
            ],
            options={
                'verbose_name_plural': 'Sucursales',
            },
        ),
        migrations.CreateModel(
            name='CompanyEmployees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthdate', models.DateField(verbose_name='fecha de nacimiento')),
                ('imss', models.IntegerField(validators=[django.core.validators.MaxValueValidator(999999999999999L)])),
                ('telephone', models.CharField(blank=True, max_length=15, null=True, verbose_name='tel\xe9fono')),
                ('salary', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='salario')),
                ('num_employee', models.IntegerField(verbose_name='numero de empleado')),
                ('studies', models.CharField(choices=[('AN', 'Ninguno'), ('EL', 'Primaria'), ('HS', 'Secundaria'), ('CL', 'Universidad')], default='AN', max_length=2, verbose_name='grado de estudios')),
                ('sex', models.CharField(choices=[('M', 'Hombre'), ('F', 'Mujer')], default='M', max_length=1, verbose_name='sexo')),
                ('curp', models.CharField(blank=True, max_length=18, null=True)),
                ('civil_status', models.CharField(choices=[('SG', 'Soltero'), ('MR', 'Casado'), ('FU', 'Union libre'), ('DV', 'Divorciado'), ('WW', 'Viudo')], default='SG', max_length=2, verbose_name='estado civl')),
                ('branch', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='companies.BranchCompany')),
            ],
            options={
                'verbose_name_plural': 'Empleados',
            },
        ),
        migrations.CreateModel(
            name='CompanyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='profiles', verbose_name='logotipo')),
                ('RFC', models.CharField(blank=True, max_length=13, null=True)),
                ('telephone', models.CharField(blank=True, max_length=15, null=True, verbose_name='tel\xe9fono')),
                ('ceo', models.CharField(blank=True, max_length=50, null=True, verbose_name='Director')),
                ('activity', models.ManyToManyField(to='companies.ActivityCatalog', verbose_name='actividades relacionadas')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='compa\xf1ia')),
            ],
            options={
                'verbose_name_plural': 'Compa\xf1\xeda',
            },
        ),
        migrations.CreateModel(
            name='DepartmentsCatalog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=30, verbose_name='departamento')),
                ('activities', models.CharField(max_length=120, verbose_name='actividad')),
            ],
            options={
                'verbose_name_plural': 'Catalogo de departamentos',
            },
        ),
        migrations.CreateModel(
            name='JobCatalog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.CharField(max_length=40, verbose_name='puesto')),
                ('description', models.CharField(max_length=200, verbose_name='descripci\xf3n')),
                ('category', models.CharField(choices=[('JR', 'Junior'), ('SS', 'Semisenior'), ('SR', 'Senior')], default='JR', max_length=2, verbose_name='categor\xeda')),
            ],
            options={
                'verbose_name_plural': 'Catalogo de puestos',
            },
        ),
        migrations.AddField(
            model_name='companyemployees',
            name='department',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='companies.DepartmentsCatalog'),
        ),
        migrations.AddField(
            model_name='companyemployees',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='empleado'),
        ),
        migrations.AddField(
            model_name='companyemployees',
            name='job',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='companies.JobCatalog'),
        ),
        migrations.AddField(
            model_name='branchcompany',
            name='manager',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='companies.CompanyEmployees'),
        ),
    ]
