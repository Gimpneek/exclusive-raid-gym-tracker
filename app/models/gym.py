# -*- coding: utf-8 -*-
""" Model definition for Gym """
from datetime import datetime
from django.db import models
from django.apps import apps
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

    def __str__(self):
        return self.name

    def get_raid_information(self):
        """
        Calculate if raid is currently active and if so return dictionary of
        values for use in template
        :return: dictionary of raid data or None
        """
        # Search raids that are on this gym and are set in the future
        time_now = datetime.now(tz=pytz.timezone('Europe/London'))
        raid_model = apps.get_model('app', 'RaidItem')
        raids = raid_model.objects.filter(
            gym=self,
            end_date__gt=time_now
        ).order_by('end_date')
        if raids:
            return raids.last().get_raid(time_now)
        return {}
