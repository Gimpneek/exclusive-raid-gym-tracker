# -*- coding: utf-8 -*-
""" Form definition for Gym Item """
from app.models.gym_item import GymItem
from django.forms.models import ModelForm


class GymItemForm(ModelForm):
    """ Gym Item form"""

    class Meta(object):
        """ Metaclass for Gym Item form """
        model = GymItem
        fields = ('last_visit_date',)
