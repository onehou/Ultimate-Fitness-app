# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-24 06:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ultimatefitbackend', '0023_remove_foodtype_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='food',
            options={'get_latest_by': 'creation_date', 'verbose_name_plural': 'foods'},
        ),
    ]