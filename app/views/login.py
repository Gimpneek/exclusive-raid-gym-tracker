# -*- coding: utf-8 -*-
""" Views for login page """
from logging import getLogger
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render


LOGGER = getLogger(__name__)


def login_page(request):
    """
    Show login form for GET & failed login. If POST then attempt to login
    """
    failed = False
    if request.user.id:
        return redirect('gym_list')
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user=user)
            return redirect('gym_list')
        else:
            LOGGER.warning(
                'Incorrect login for %s', request.POST.get('username'))
            failed = True
    return render(
        request,
        'app/login.html',
        {
            'failed': failed
        }
    )
