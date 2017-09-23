# -*- coding: utf-8 -*-
""" Views for User Profile """
from os import environ
from calendar import day_name
from datetime import datetime, timedelta, date
from collections import Counter
from django.shortcuts import render
from app.models.raid_item import RaidItem
from app.views.common import create_js_obj_from_loc
import pytz


def analytics_dashboard(request):
    """
    Show analytics for raids in Leeds
    :param request: Web Request
    :return: Webpage showing analytics
    """
    now = datetime.combine(date.today(), datetime.min.time())\
        .astimezone(pytz.UTC)
    one_week_ago = now + timedelta(weeks=-1)
    raids = RaidItem.objects.filter(
        end_date__gte=one_week_ago
    )
    gym_list = []
    level_list = []
    day_list = []
    hour_list = []
    for raid in raids:
        gym_list.append(raid.gym.name)
        level_list.append(raid.level)
        day_list.append(day_name[raid.end_date.weekday()])
        raid_end = raid.end_date.astimezone(pytz.timezone('Europe/London'))
        hour_list.append((raid_end - timedelta(hours=1)).hour)
    busiest_gyms = Counter(gym_list).most_common()
    if len(busiest_gyms) > 10:
        busiest_gyms = busiest_gyms[:10]
    raid_levels = Counter(level_list).most_common()
    busiest_hours = Counter(hour_list).most_common()
    busiest_days = Counter(day_list).most_common()
    return render(request, 'app/analytics_dashboard.html', {
        'start_date': one_week_ago,
        'end_date': now,
        'raids': raids,
        'most_active_gym': busiest_gyms[0][0] if busiest_gyms else 'N/A',
        'most_active_hour': busiest_hours[0][0] if busiest_hours else 'N/A',
        'most_active_day': busiest_days[0][0] if busiest_days else 'N/A',
        'active_gyms': busiest_gyms,
        'active_levels': raid_levels,
        'active_days': busiest_days,
        'active_hours': busiest_hours,
        'active_gym_markers': get_active_gyms_as_js(busiest_gyms, raids),
        'map_key': environ.get('MAPS_API_KEY'),
    })


def get_active_gyms_as_js(gyms, raids):
    """
    Using the supplied raids return a list of JS objects for use in template
    :param gyms: List of gyms to turn into JS objects
    :param raids: List of raids
    :return: string of json
    """
    js_objs = []
    for gym in gyms:
        raid = [raid for raid in raids if raid.gym.name == gym[0]][0]
        js_objs.append(create_js_obj_from_loc(raid.gym.location))
    return '[{}]'.format(','.join(js_objs))
