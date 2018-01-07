# -*- coding: utf-8 -*-
""" Views for homepage """
from django.shortcuts import render


def index(request):
    """
    Show the homepage
    """
    return render(request, 'app/index.html')
