# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models.gym import Gym
from models.gym_item import GymItem
from models.profile import Profile

# Register your models here.
admin.site.register(Gym)
admin.site.register(GymItem)
admin.site.register(Profile)
