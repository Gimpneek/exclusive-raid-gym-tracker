# -*- coding: utf-8 -*-
""" Views for Gym List """
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import F
from app.models.gym_item import GymItem
from app.models.profile import Profile


@login_required
def gym_list(request):
    """
    Show the Gym List
    """
    profile = Profile.objects.get(
        user=request.user.id
    )
    gym_item_list = GymItem.objects.filter(
        profile=profile.id,
        hidden=False
    ).order_by(
        F('last_visit_date').asc(nulls_first=True),
        'gym__name'
    )
    total_gyms = len(gym_item_list)
    completed_gyms = [gym for gym in gym_item_list if gym.last_visit_date]
    gyms_to_visit = [gym for gym in gym_item_list if not gym.last_visit_date]
    gyms_to_visit = sorted(
        gyms_to_visit,
        key=lambda k: k.get_raid_information.get('time_left', ''),
        reverse=True
    )
    gym_progress = 0
    if completed_gyms:
        gym_progress = int((float(len(completed_gyms))/float(total_gyms))*100)
    return render(request, 'app/gym_list.html', {
        'completed_gym_list': completed_gyms,
        'gyms_to_visit': gyms_to_visit,
        'total_gyms': total_gyms,
        'completed_gym_count': len(completed_gyms),
        'gym_progress': gym_progress
    })
