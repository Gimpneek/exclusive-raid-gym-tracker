# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-22 21:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20170822_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gymitem',
            name='last_visit_date',
            field=models.DateField(
                blank=True,
                help_text=b'Date of last visit',
                null=True
            ),
        ),
    ]
