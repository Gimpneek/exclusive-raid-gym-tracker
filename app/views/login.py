# -*- coding: utf-8 -*-
""" Views for login page """
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render


def login_page(request):
    """
    Show login form for GET & failed login. If POST then attempt to login
    """
    failed = False
    if request.user.id:
        return redirect('gym_list')
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user=user)
            return redirect('gym_list')
        else:
            failed = True
    return render(
        request,
        'app/login.html',
        {
            'failed': failed
        }
    )
