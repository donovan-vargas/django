# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-15 13:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20160614_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddress',
            name='CP',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.PostalCodeCatalog'),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.CitiesCatalog'),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.StatesCatalog'),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='suburb',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.SuburbCatalog'),
        ),
    ]
