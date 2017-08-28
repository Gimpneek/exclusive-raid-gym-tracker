# -*- coding: utf-8 -*-
""" Form definition for User """
from django.contrib.auth.models import User
from django.forms.models import ModelForm


class UserForm(ModelForm):
    """ User form """

    class Meta(object):
        """ Metaclass for User form """
        model = User
        fields = ('username', 'password')
