# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-20 12:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products_module', '0003_produits_numero_lot'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=80)),
                ('description', models.CharField(blank=True, max_length=160)),
                ('origine', models.CharField(max_length=50)),
                ('ean', models.CharField(blank=True, max_length=13)),
                ('numero_lot', models.CharField(blank=True, max_length=10)),
                ('prix_achat', models.DecimalField(decimal_places=2, max_digits=6)),
                ('prix_revente_gros', models.DecimalField(decimal_places=2, max_digits=6)),
                ('prix_revente_particuliers', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.DeleteModel(
            name='Produits',
        ),
    ]
