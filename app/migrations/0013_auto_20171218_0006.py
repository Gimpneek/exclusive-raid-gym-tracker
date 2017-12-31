# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-18 00:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_gymitem_gym_visit_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='tracked_gyms',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to='app.Gym'
            ),
        ),
    ]
