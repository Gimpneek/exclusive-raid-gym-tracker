# -*- coding: utf-8 -*-
""" Views for Gym List """
import operator
from functools import reduce
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from app.models.gym_item import GymItem
from app.models.gym import Gym
from app.models.profile import Profile


@login_required
def gym_list(request):
    """
    Show the Gym List
    """
    profile = Profile.objects.get(
        user=request.user.id
    )
    gyms = Gym.objects.all().order_by('name')
    total_gyms = gyms.count()
    completed_gyms = GymItem.objects.filter(
        profile=profile,
        gym_visit_date__isnull=False
    )
    completed_gym_names = set([gym.gym.name for gym in completed_gyms])
    completed_gym_count = len(completed_gym_names)
    if completed_gym_names:
        completed_gym_filter = reduce(
            operator.or_,
            (Q(name=x) for x in completed_gym_names)
        )
        gyms_with_visits = Gym.objects.filter(completed_gym_filter)
        yet_to_visit = \
            Gym.objects.exclude(completed_gym_filter).order_by('name')
    else:
        gyms_with_visits = []
        yet_to_visit = gyms
    gyms_to_visit = []
    completed_gyms = []
    raids_active = []
    for gym in yet_to_visit:
        if gym.get_raid_information().get('time_left'):
            raids_active.append(gym)
        else:
            gyms_to_visit.append(gym)
    for gym in gyms_with_visits:
        if gym.get_raid_information().get('time_left'):
            raids_active.append(gym)
        else:
            completed_gyms.append(gym)
    raids_active = sorted(
        raids_active,
        key=lambda k: k.get_raid_information().get('time_left', '')
    )
    completed_gyms = sorted(
        completed_gyms,
        key=lambda k: GymItem.objects.filter(
            profile=profile, gym=k).last().gym_visit_date
    )
    gym_progress = 0
    if completed_gyms:
        gym_progress = int((float(completed_gym_count)/float(total_gyms))*100)
    return render(request, 'app/gym_list.html', {
        'active_raids': raids_active,
        'completed_gym_list': completed_gyms,
        'gyms_to_visit': gyms_to_visit,
        'total_gyms': total_gyms,
        'completed_gym_count': completed_gym_count,
        'gym_progress': gym_progress,
        'user_id': request.user.id
    })
