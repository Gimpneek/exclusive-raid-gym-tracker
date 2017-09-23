# -*- coding: utf-8 -*-
""" Model definition for Raid"""
from datetime import datetime
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from app.models.gym import Gym
import pytz


@python_2_unicode_compatible
class RaidItem(models.Model):
    """ Model to hold Raid information """

    pokemon = models.CharField(
        max_length=128,
        help_text="Name of Raid Pokemon",
        blank=True,
        null=True
    )

    level = models.PositiveSmallIntegerField(
        help_text="Level of Raid",
        blank=True,
        null=True
    )

    end_date = models.DateTimeField(
        help_text="End Date of Raid",
        blank=True,
        null=True
    )

    gym = models.ForeignKey(
        Gym,
        help_text="Gym raid is on"
    )

    def __str__(self):
        return '{} on {}'.format(self.pokemon, self.gym.name)

    def get_raid(self, starting_dt=None):
        """
        Calculate if raid is currently active and if so return dictionary of
        values for use in template
        :param starting_dt: Datetime to calculate from
        :return: dictionary of raid data or None
        """
        if not starting_dt:
            starting_dt = datetime.now(tz=pytz.timezone('Europe/London'))
        if self.end_date and self.level:
            time_left = self.end_date - starting_dt
            if time_left.total_seconds() > 0:
                pokemon = 'Egg'
                if self.pokemon:
                    pokemon = self.pokemon
                return {
                    'pokemon': pokemon,
                    'level': self.level,
                    'time_left': '{} remaining'.format(
                        datetime
                        .fromtimestamp(time_left.seconds)
                        .strftime('%-H:%M:%S')
                    )
                }
        return {}
