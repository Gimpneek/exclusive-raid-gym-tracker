# -*- coding: utf-8 -*-
""" Views for Logging user out """
from django.contrib.auth import logout
from django.shortcuts import redirect


def logout_page(request):
    """ Log the user out and redirect to homepage """
    logout(request)
    return redirect('index')
