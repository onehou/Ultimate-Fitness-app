# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-11 17:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=320)),
                ('address', models.TextField()),
                ('phone', models.TextField()),
                ('history', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=320)),
                ('pub_date', models.DateTimeField(blank=True, null=True, verbose_name='date published')),
                ('pub_date_string', models.CharField(blank=True, max_length=320, null=True)),
                ('description', models.TextField()),
                ('image', models.TextField(blank=True, null=True)),
                ('price', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'foods',
            },
        ),
        migrations.CreateModel(
            name='FoodCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=320)),
                ('image', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=320)),
                ('description', models.TextField()),
                ('image', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='MenuCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=320)),
                ('description', models.TextField()),
                ('image', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=320, null=True)),
                ('order_date', models.DateTimeField(blank=True, null=True, verbose_name='date published')),
                ('payment_type', models.CharField(blank=True, max_length=100, null=True)),
                ('payment_id', models.CharField(blank=True, max_length=100, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ultimatefitbackend.Customer')),
            ],
        ),
        migrations.AddField(
            model_name='menu',
            name='menucategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ultimatefitbackend.MenuCategory'),
        ),
        migrations.AddField(
            model_name='food',
            name='foodcategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ultimatefitbackend.FoodCategory'),
        ),
        migrations.AddField(
            model_name='food',
            name='menu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ultimatefitbackend.Menu'),
        ),
        migrations.AddField(
            model_name='food',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ultimatefitbackend.Order'),
        ),
    ]