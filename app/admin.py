# -*- coding: utf-8 -*-
""" Expose models to the admin view """
from __future__ import unicode_literals

from django.contrib import admin
from app.models.gym import Gym
from app.models.gym_item import GymItem
from app.models.profile import Profile
from app.models.raid_item import RaidItem
from app.models.ex_raid_pokemon import ExRaidPokemon

# Register your models here.
admin.site.register(Gym)
admin.site.register(GymItem)
admin.site.register(Profile)
admin.site.register(RaidItem)
admin.site.register(ExRaidPokemon)
