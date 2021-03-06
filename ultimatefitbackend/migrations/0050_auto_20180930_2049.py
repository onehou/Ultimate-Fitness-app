# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-09-30 12:49
from __future__ import unicode_literals

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ultimatefitbackend', '0049_couponpromotion_available_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='couponpromotion',
            name='available_categories',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('PERCENTAGE', 'Percentage (x%)'), ('PERCENTAGEWITHCAP', 'Percentage with cap (x%, capped at $y)'), ('ABSOLUTEWITHMIN', 'Absolute with min ($x, min $y)')], max_length=100),
        ),
    ]
