# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-23 16:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_auto_20171223_1608'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExRaidPokemon',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID'
                    )
                ),
                (
                    'name', models.CharField(
                        help_text='Name of EX-Raid Pokemon',
                        max_length=256
                    )
                ),
            ],
        ),
    ]
