""" Serializer for Gym Item model """
from app.models.gym_item import GymItem
from rest_framework import serializers


class GymItemSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializer for Gym Item model """
    class Meta:
        model = GymItem
        fields = 'gym_visit_date'
