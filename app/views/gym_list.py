# -*- coding: utf-8 -*-
""" Views for Gym List """
import operator
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
        last_visit_date__isnull=False
    )
    completed_gym_names = set([gym.gym.name for gym in completed_gyms])
    if completed_gym_names:
        completed_gym_filter = reduce(
            operator.or_,
            (Q(name=x) for x in completed_gym_names)
        )
        completed_gyms = \
            Gym.objects.filter(completed_gym_filter).order_by('name')
        yet_to_visit = \
            Gym.objects.exclude(completed_gym_filter).order_by('name')
    else:
        completed_gyms = []
        yet_to_visit = gyms
    gyms_to_visit = []
    raids_active = []
    for gym in yet_to_visit:
        if gym.get_raid_information().get('time_left'):
            raids_active.append(gym)
        else:
            gyms_to_visit.append(gym)
    raids_active = sorted(
        raids_active,
        key=lambda k: k.get_raid_information().get('time_left', '')
    )
    gyms_to_visit = raids_active + gyms_to_visit
    gym_progress = 0
    if completed_gyms:
        gym_progress = int((float(len(completed_gyms))/float(total_gyms))*100)
    return render(request, 'app/gym_list.html', {
        'completed_gym_list': completed_gyms,
        'gyms_to_visit': gyms_to_visit,
        'total_gyms': total_gyms,
        'completed_gym_count': len(completed_gyms),
        'gym_progress': gym_progress,
        'user_id': request.user.id
    })
