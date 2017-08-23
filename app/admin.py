# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from app.models.gym import Gym
from app.models.gym_item import GymItem
from app.models.profile import Profile

# Register your models here.
admin.site.register(Gym)
admin.site.register(GymItem)
admin.site.register(Profile)
