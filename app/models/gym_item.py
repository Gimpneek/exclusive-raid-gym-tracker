# -*- coding: utf-8 -*-
""" Model definition for Gym Item """
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from app.models.gym import Gym
from app.models.profile import Profile


@python_2_unicode_compatible
class GymItem(models.Model):
    """ Item in users list for Gym """

    last_visit_date = models.DateField(
        help_text="Date of last visit",
        blank=True,
        null=True
    )
    gym_visit_date = models.DateTimeField(
        help_text="Date visited gym",
        blank=True,
        null=True
    )
    hidden = models.BooleanField(
        help_text="Hide this gym?",
        default=False
    )
    gym = models.ForeignKey(
        Gym,
        help_text="Gym item is for",
        on_delete=models.DO_NOTHING
    )
    profile = models.ForeignKey(
        Profile,
        help_text="Profile gym item is associated with",
        on_delete=models.DO_NOTHING
    )

    def __str__(self):
        return "{} - {}".format(
            self.profile.user.username,
            self.gym.name
        )
