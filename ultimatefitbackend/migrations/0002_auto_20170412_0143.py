# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-11 17:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ultimatefitbackend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='stock',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='food',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]
