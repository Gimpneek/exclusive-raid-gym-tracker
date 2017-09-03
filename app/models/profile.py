# -*- coding: utf-8 -*-
""" Model definition of User Profile """
from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Profile(models.Model):
    """ Profile for user """
    user = models.OneToOneField(User)
    pokemon_go_username = models.CharField(
        max_length=128,
        help_text="Your name in Pokemon Go",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.user.username
