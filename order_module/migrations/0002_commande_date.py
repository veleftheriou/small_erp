# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-04 06:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('order_module', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='commande',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
