# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-15 22:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('accounts', '0007_suburbcatalog_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraddress',
            name='number',
            field=models.CharField(default=532, max_length=30),
            preserve_default=False,
        ),
    ]
