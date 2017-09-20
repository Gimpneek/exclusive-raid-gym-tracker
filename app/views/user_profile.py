# -*- coding: utf-8 -*-
""" Views for User Profile """
from os import environ
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
        gym_visit_date__isnull=False
    ).order_by('gym_visit_date')
    return render(request, 'app/profile.html', {
        'profile': profile,
        'completed_raids': raids,
        'map_url': create_map_img(raids),
        'map_key': environ.get('MAPS_API_KEY'),
        'raid_markers': get_raids_as_js(raids)
    })


def create_map_img(raids):
    """
    Using the provided raids create a img URL for them
    :param raids: list of raid items to show on map
    :return: URL to image
    """
    url = 'https://maps.googleapis.com/maps/api/staticmap' \
          '?center=53.7954869,-1.5460196' \
          '&zoom=14' \
          '&scale=2' \
          '&size=600x300' \
          '&maptype=roadmap' \
          '&key={}'.format(environ.get('MAPS_API_KEY'))
    for raid in raids:
        url += '&markers=color:red%7C{}'.format(raid.gym.location)
    return url


def get_raids_as_js(raids):
    """
    Using the supplied raids return a list of JS objects for use in template
    :param raids: List of raids to turn into JS objects
    :return: string of json
    """
    js_objs = []
    for raid in raids:
        raid_loc = raid.gym.location.split(',')
        obj_str = '{'
        obj_str += 'lat: {0},lng: {1}'.format(raid_loc[0], raid_loc[1])
        obj_str += '}'
        js_objs.append(obj_str)
    return '[{}]'.format(','.join(js_objs))
