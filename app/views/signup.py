# -*- coding: utf-8 -*-
""" Views for Sign up form """
from logging import getLogger
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from app.models.profile import Profile
from app.forms.user import UserForm


LOGGER = getLogger(__name__)


def signup_page(request):
    """
    Show Sign up page for GET request. If unable to create account then show
    errors. If successful then redirect to the Gym List
    """
    failed = False
    if request.user.id:
        return redirect('gym_list')
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            Profile.objects.create(user=new_user)
            login(request, new_user)
            return redirect('gym_list')
        else:
            LOGGER.warning(
                'Issues signed up with %s',  form.data.get('username'))
            failed = str(form.errors)
    else:
        form = UserForm()
    return render(
        request,
        'app/signup.html',
        {
            'form': form,
            'failed': failed
        }
    )
