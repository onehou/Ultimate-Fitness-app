# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-07 17:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ultimatefitbackend', '0007_cart_session_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cart', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='cart',
            unique_together=set([('user', 'session_key')]),
        ),
    ]
