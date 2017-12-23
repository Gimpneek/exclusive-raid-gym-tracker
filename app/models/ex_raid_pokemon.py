# -*- coding: utf-8 -*-
""" Model definition for EX-Raid Pokemon """
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class ExRaidPokemon(models.Model):
    """ Model to hold the name of EX-Raid Pokemon """

    name = models.CharField(
        max_length=256,
        help_text="Name of EX-Raid Pokemon"
    )

    def __str__(self):
        return self.name
