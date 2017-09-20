# -*- coding: utf-8 -*-
""" Form definition for Gym Item """
from app.models.gym_item import GymItem
from django.forms.models import ModelForm
from django.forms import DateTimeField


class GymItemForm(ModelForm):
    """ Gym Item form"""

    gym_visit_date = DateTimeField(input_formats=['%Y-%m-%dT%H:%M'])

    class Meta(object):
        """ Metaclass for Gym Item form """
        model = GymItem
        fields = ('gym_visit_date',)
