# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-23 16:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_auto_20171221_2300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gymlist',
            name='gyms',
        ),
        migrations.RemoveField(
            model_name='gymlist',
            name='profile',
        ),
        migrations.DeleteModel(
            name='GymList',
        ),
    ]
