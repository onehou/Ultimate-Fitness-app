# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-22 15:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ultimatefitbackend', '0016_remove_menu_food_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fooditem',
            name='food',
        ),
        migrations.DeleteModel(
            name='FoodItem',
        ),
    ]
