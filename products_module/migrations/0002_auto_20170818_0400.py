# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-18 02:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products_module', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produits',
            name='ean',
            field=models.CharField(max_length=13, null=True),
        ),
    ]
