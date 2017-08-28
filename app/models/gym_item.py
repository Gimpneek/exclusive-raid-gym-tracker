# -*- coding: utf-8 -*-
""" Model definition for Gym Item """
from django.db import models
from app.models.gym import Gym
from app.models.profile import Profile


class GymItem(models.Model):
    """ Item in users list for Gym """

    last_visit_date = models.DateField(
        help_text="Date of last visit",
        blank=True,
        null=True
    )
    hidden = models.BooleanField(
        help_text="Hide this gym?",
        default=False
    )
    gym = models.ForeignKey(
        Gym,
        help_text="Gym item is for"
    )
    profile = models.ForeignKey(
        Profile,
        help_text="Profile gym item is associated with"
    )

    def __str__(self):
        return "{} - {}".format(
            self.profile.user.username,
            self.gym.name
        )
