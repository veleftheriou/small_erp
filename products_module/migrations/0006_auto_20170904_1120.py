# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-04 09:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products_module', '0005_stock'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='produit',
        ),
        migrations.AddField(
            model_name='produit',
            name='stock',
            field=models.IntegerField(default=0, max_length=3),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Stock',
        ),
    ]
