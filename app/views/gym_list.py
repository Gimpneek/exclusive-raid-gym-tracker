# -*- coding: utf-8 -*-
""" Views for Gym List """
from django.shortcuts import render, redirect
from django.core.exceptions import SuspiciousOperation
from django.contrib.auth.decorators import login_required
from app.models.gym import Gym
from app.models.profile import Profile


@login_required
def gym_list(request):
    """
    Show the Gym List
    """
    profile = Profile.objects.get(user=request.user)
    gyms = Gym.objects.all().order_by('name')
    return render(request, 'app/gym_list.html', {
        'gym_list': gyms,
        'tracked_gyms': profile.tracked_gyms.all(),
        'user_id': request.user.id
    })


@login_required
def raid_list(request):
    """
    Show the Gym List
    """
    profile = Profile.objects.get(user=request.user)
    gyms = profile.tracked_gyms.all()
    raids_active = \
        [gym for gym in gyms if gym.get_raid_information().get('time_left')]
    raids_active = sorted(
        raids_active,
        key=lambda k: k.get_raid_information().get('time_left', '')
    )
    return render(request, 'app/active_raids.html', {
        'active_raids': raids_active,
        'user_id': request.user.id
    })


@login_required
def gym_management(request):
    """
    Show list of tracked gyms so user can add or remove them

    :param request: HTTP Request
    :return: List of gyms being tracked by currently logged in user
    """
    profile = Profile.objects.get(user=request.user)
    gyms = Gym.objects.all().order_by('name')
    return render(request, 'app/gym_management.html', {
        'gym_list': gyms,
        'tracked_gyms': profile.tracked_gyms.all(),
        'user_id': request.user.id
    })


@login_required
def add_tracked_gym(request, gym_id):
    """
    Add the requested Gym to the currently logged in user's list of tracked
    Gyms

    :param request: HTTP Request
    :param gym_id: ID of the gym to add
    :return: Redirect to Gym Management Page
    """
    requested_gym = Gym.objects.get(id=gym_id)
    profile = Profile.objects.get(user=request.user)
    if requested_gym not in profile.tracked_gyms.all():
        profile.tracked_gyms.add(requested_gym)
        profile.save()
    return redirect('gym_management')


@login_required
def remove_tracked_gym(request, gym_id):
    """
    Remove the requested Gym from the currently logged in user's list of
    tracked Gyms

    :param request: HTTP Request
    :param gym_id: ID of the gym to remove
    :return: Redirect to Gym Management Page
    """
    requested_gym = Gym.objects.get(id=gym_id)
    profile = Profile.objects.get(user=request.user)
    if requested_gym in profile.tracked_gyms.all():
        profile.tracked_gyms.remove(requested_gym)
        profile.save()
        return redirect('gym_management')
    raise SuspiciousOperation
