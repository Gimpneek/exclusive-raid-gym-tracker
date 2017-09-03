# -*- coding: utf-8 -*-
""" Model definition for Gym """
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Gym(models.Model):
    """ Model to hold Gym information """

    name = models.CharField(
        max_length=256,
        help_text="Name of Gym"
    )
    gym_hunter_id = models.CharField(
        max_length=32,
        help_text="ID on Gymhuntr",
        blank=True,
        null=True
    )
    location = models.CharField(
        max_length=128,
        help_text="Location in long,lat format"
    )
    image_url = models.CharField(
        max_length=256,
        help_text="URL of image used for Gym",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name
