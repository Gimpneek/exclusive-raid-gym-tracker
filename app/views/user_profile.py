# -*- coding: utf-8 -*-
""" Views for User Profile """
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app.models.profile import Profile
from app.models.gym_item import GymItem


@login_required
def user_profile(request):
    """
    Show the user's profile
    :param request:
    :return:
    """
    profile = Profile.objects.get(
        user=request.user.id
    )
    raids = GymItem.objects.filter(
        profile=profile,
        last_visit_date__isnull=False
    ).order_by('last_visit_date')
    return render(request, 'app/profile.html', {
        'profile': profile,
        'completed_raids': raids
    })
