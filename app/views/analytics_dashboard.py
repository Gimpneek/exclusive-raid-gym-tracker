# -*- coding: utf-8 -*-
""" Views for User Profile """
from os import environ
from calendar import day_name
from datetime import datetime, timedelta, date
from django.shortcuts import render
from django.db.models import Count
from django.db.models.functions import ExtractWeekDay, ExtractHour
from app.models.raid_item import RaidItem
from app.models.gym import Gym
from app.views.common import create_js_obj_from_loc
import pytz


def analytics_dashboard(request):
    """
    Show analytics for raids in Leeds
    :param request: Web Request
    :return: Webpage showing analytics
    """
    now = datetime.combine(date.today(), datetime.min.time())\
        .replace(tzinfo=pytz.UTC)
    one_week_ago = now + timedelta(weeks=-1)
    raids = RaidItem.objects.filter(
        end_date__gte=one_week_ago
    ).values_list("id", flat=True)
    gym_list = RaidItem.objects\
        .filter(id__in=raids)\
        .values("gym__name", "gym__id")\
        .annotate(Count("id"))\
        .order_by("-id__count")[:10]
    level_list = RaidItem.objects\
        .filter(id__in=raids)\
        .values("level")\
        .annotate(Count("id"))\
        .order_by("-id__count")
    day_list = RaidItem.objects.annotate(weekday=ExtractWeekDay("end_date")).values("weekday").annotate(Count("weekday")).order_by("-weekday__count")
    hour_list = RaidItem.objects\
        .filter(id__in=raids)\
        .annotate(hour=ExtractHour("end_date"))\
        .values("hour")\
        .annotate(Count("hour"))\
        .order_by("-hour__count")
    return render(request, 'app/analytics_dashboard.html', {
        'start_date': one_week_ago,
        'end_date': now,
        'raids_count': raids.count(),
        'most_active_gym': gym_list[0].get("gym__name") if gym_list else 'N/A',
        'most_active_hour': hour_list[0].get("hour") if hour_list else 'N/A',
        'most_active_day':
            day_name[day_list[0].get("weekday")-1] if day_list else 'N/A',
        'active_gyms': [
            [gym.get("gym__name"), gym.get("id__count")] for gym in gym_list],
        'active_levels': [
            [lvl.get("level"), lvl.get("id__count")] for lvl in level_list],
        'active_days': [
            [day_name[day.get("weekday")-1], day.get("weekday__count")]
            for day in day_list],
        'active_hours': [
            [hour.get("hour"), hour.get("hour__count")] for hour in hour_list],
        'active_gym_markers': get_active_gyms_as_js(gym_list),
        'map_key': environ.get('MAPS_API_KEY'),
    })


def get_active_gyms_as_js(gym_list):
    """
    Using the supplied raids return a list of JS objects for use in template
    :param gym_list: List of gyms to turn into JS objects
    :return: string of json
    """
    js_objs = []
    for gym_list_item in gym_list:
        gym = Gym.objects.get(id=int(gym_list_item.get("gym__id")))
        js_objs.append(create_js_obj_from_loc(gym.location))
    return '[{}]'.format(','.join(js_objs))
