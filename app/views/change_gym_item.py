# -*- coding: utf-8 -*-
""" Views for Reseting stats on Gym """
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from app.models.gym_item import GymItem


@login_required
def reset_gym_item(request, gym_item_id):
    """
    Reset the Gym's last visit date and redirect to Gym List
    """
    gym_item = GymItem.objects.get(id=gym_item_id)
    gym_item.last_visit_date = None
    gym_item.save()
    return redirect('gym_list')


@login_required
def hide_gym_item(request, gym_item_id):
    """
    Hide the item and then redirect to list
    """
    gym_item = GymItem.objects.get(id=gym_item_id)
    gym_item.hidden = True
    gym_item.save()
    return redirect('gym_list')
