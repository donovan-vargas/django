# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-29 22:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Addresses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=150, verbose_name='Calle')),
                ('crossing_x', models.CharField(blank=True, max_length=150, null=True, verbose_name='Cruzamiento')),
                ('crossing_y', models.CharField(blank=True, max_length=150, null=True, verbose_name='Cruzamiento')),
                ('number', models.CharField(max_length=30, verbose_name='Numero')),
            ],
            options={
                'verbose_name_plural': 'Direcciones',
            },
        ),
        migrations.CreateModel(
            name='CitiesCatalog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=60, verbose_name='Ciudad')),
            ],
            options={
                'verbose_name_plural': 'Catalogo de ciudades',
            },
        ),
        migrations.CreateModel(
            name='PostalCodeCatalog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postal_code', models.CharField(max_length=10, verbose_name='C\xf3digo postal')),
            ],
            options={
                'verbose_name_plural': 'Catalogo de CP',
            },
        ),
        migrations.CreateModel(
            name='StatesCatalog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=60, verbose_name='Estado')),
            ],
            options={
                'verbose_name_plural': 'Catalogo de estados',
            },
        ),
        migrations.CreateModel(
            name='SuburbCatalog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suburb', models.CharField(max_length=100, verbose_name='Colonia')),
                ('code', models.CharField(max_length=10, verbose_name='Codigo')),
            ],
            options={
                'verbose_name_plural': 'Catalogo de colonias',
            },
        ),
        migrations.AddField(
            model_name='addresses',
            name='city',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='addresses.CitiesCatalog'),
        ),
        migrations.AddField(
            model_name='addresses',
            name='postal_code',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='addresses.PostalCodeCatalog'),
        ),
        migrations.AddField(
            model_name='addresses',
            name='state',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='addresses.StatesCatalog'),
        ),
        migrations.AddField(
            model_name='addresses',
            name='suburb',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='addresses.SuburbCatalog'),
        ),
        migrations.AddField(
            model_name='addresses',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]