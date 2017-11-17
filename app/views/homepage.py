# -*- coding: utf-8 -*-
""" Views for homepage """
from django.shortcuts import render, redirect


def index(request):
    """
    Show the homepage
    """
    if request.user.id:
        return redirect('gym_list')
    return render(request, 'app/index.html')
