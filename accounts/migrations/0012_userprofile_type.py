# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-23 21:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_delete_lakes'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='type',
            field=models.CharField(default='user', editable=False, max_length=30),
        ),
    ]
