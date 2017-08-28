# -*- coding: utf-8 -*-
""" Views for Sign up form """
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from app.models.profile import Profile
from app.models.gym import Gym
from app.models.gym_item import GymItem
from app.forms.user import UserForm


def signup_page(request):
    """
    Show Sign up page for GET request. If unable to create account then show
    errors. If successful then redirect to the Gym List
    """
    failed = False
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            profile = Profile.objects.create(user=new_user)
            gyms = Gym.objects.all()
            for gym in gyms:
                GymItem.objects.create(gym=gym, profile=profile)
            login(request, new_user)
            return redirect('gym_list')
        else:
            failed = True
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
