""" Common helper functions for the viewsets """
from rest_framework import status
from rest_framework.response import Response
from app.serializers.raid_item import RaidItemSerializer
from app.serializers.gym_item import GymItemSerializer
from app.models.gym_item import GymItem
from app.models.gym import Gym
from app.models.profile import Profile
from app.forms.gym_item import GymItemForm
import pytz


def get_raid_response(request, queryset):
    """
    Generate the response for the raid endpoints

    :param request: Django request
    :param queryset: RaidItem queryset
    :return: Django Rest Framework Response
    """
    serializer = RaidItemSerializer(
        queryset,
        many=True,
        context={'request': request}
    )
    return Response(serializer.data)


def create_gym_visit(request, gym_id=None):
    """
    Create a GymItem object with the supplied values

    :param request: Django Request
    :param gym_id: ID for Gym
    :return: Django Rest Framework Response
    """
    form = GymItemForm(request.data)
    if form.is_valid():
        gym_visit_date = form.cleaned_data.get('gym_visit_date') \
            .replace(tzinfo=pytz.timezone('Europe/London'))
        profile = Profile.objects.get(user=request.user.id)
        if gym_id:
            gym = Gym.objects.get(pk=gym_id)
        else:
            gym = Gym.objects.get(pk=form.data.get('gym'))
        GymItem.objects.create(
            gym=gym,
            profile=profile,
            gym_visit_date=gym_visit_date
        )
        if gym not in profile.tracked_gyms.all():
            profile.tracked_gyms.add(gym)
            profile.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


def paginate_raids(instance, request, queryset):
    """
    Paginate the results for the raid list

    :param instance: Class instance
    :param request: Django request
    :param queryset: queryset to paginate
    :return: paginated list of results or normal one
    """
    page = instance.paginate_queryset(queryset)
    if page is not None:
        serializer = instance.get_serializer(page, many=True)
        return instance.get_paginated_response(serializer.data)
    return get_raid_response(request, queryset)


def paginate_gym_items(instance, queryset):
    """
    Paginate the results of the gym visit lists

    :param instance: Class instance
    :param queryset: queryset to paginate
    :return: paginated list of results or normal one
    """
    page = instance.paginate_queryset(queryset)
    if page is not None:
        serializer = instance.get_serializer(page, many=True)
        return instance.get_paginated_response(serializer.data)
    serializer = GymItemSerializer(queryset, many=True)
    return Response(serializer.data)
