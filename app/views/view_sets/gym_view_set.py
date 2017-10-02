# pylint: disable=too-many-ancestors
""" View Set for Gym Serializer """
from rest_framework import viewsets
from app.models.gym import Gym
from app.serializers.gym import GymSerializer


class GymViewSet(viewsets.ReadOnlyModelViewSet):
    """
    View Set for Gym Serializer
    """

    queryset = Gym.objects.all().order_by('name')
    serializer_class = GymSerializer
