# -*- coding: utf-8 -*-
""" Model definition for Gym """
from datetime import datetime
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import pytz


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

    raid_pokemon = models.CharField(
        max_length=128,
        help_text="Name of Raid Pokemon",
        blank=True,
        null=True
    )

    raid_level = models.PositiveSmallIntegerField(
        help_text="Level of Raid",
        blank=True,
        null=True
    )

    raid_end_date = models.DateTimeField(
        help_text="End Date of Raid",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name

    def get_raid_information(self, starting_dt=None):
        """
        Calculate if raid is currently active and if so return dictionary of
        values for use in template
        :param starting_dt: Datetime to calculate from
        :return: dictionary of raid data or None
        """
        if not starting_dt:
            starting_dt = datetime.now(tz=pytz.utc)
        if self.raid_end_date and self.raid_level and self.raid_pokemon:
            time_left = self.raid_end_date - starting_dt
            if time_left.total_seconds() > 0:
                return {
                    'pokemon': self.raid_pokemon,
                    'level': self.raid_level,
                    'time_left': '{} remaining'.format(time_left)
                }
        return None
