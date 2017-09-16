# -*- coding: utf-8 -*-
""" Views for Reseting stats on Gym """
from datetime import datetime
from logging import getLogger
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from app.models.gym_item import GymItem
from app.models.profile import Profile
from app.models.gym import Gym
from app.forms.gym_item import GymItemForm


LOGGER = getLogger(__name__)


@login_required
def reset_gym_item(request, gym_item_id):
    """
    Reset the Gym's last visit date and redirect to Gym List
    """
    gym_item = GymItem.objects.get(id=gym_item_id)
    if gym_item.profile.user.id != request.user.id:
        LOGGER.info(
            'User %s tried to reset gym '
            'that didn\'t belong to them' % request.user.username
        )
        return redirect('gym_list')
    gym_item.last_visit_date = None
    gym_item.save()
    return redirect('gym_list')


@login_required
def hide_gym_item(request, gym_item_id):
    """
    Hide the item and then redirect to list
    """
    gym_item = GymItem.objects.get(id=gym_item_id)
    if gym_item.profile.user.id != request.user.id:
        LOGGER.info(
            'User %s tried to hide gym '
            'that didn\'t belong to them' % request.user.username
        )
        return redirect('gym_list')
    gym_item.hidden = True
    gym_item.save()
    return redirect('gym_list')


@login_required
def add_gym_raid(request, gym_id):
    """
    Add a raid on a gym
    :param request: HTTP Request
    :param gym_id: ID of the gym to add raid for
    :return: Form or redirect
    """
    requested_gym = Gym.objects.get(id=gym_id)
    failed = False
    if request.POST:
        form = GymItemForm(request.POST)
        if form.is_valid():
            last_visit_date = request.POST['last_visit_date']
            profile = Profile.objects.get(user=request.user.id)
            GymItem.objects.create(
                gym=requested_gym,
                profile=profile,
                last_visit_date=last_visit_date
            )
            return redirect('gym_list')
        else:
            LOGGER.warning('Invalid date added to gym update')
            failed = True
    else:
        form = GymItemForm()
    return render(request, 'app/add_gym_raid.html', {
        'gym': requested_gym,
        'form': form,
        'date_to_show': datetime.now(),
        'failed': failed
    })
