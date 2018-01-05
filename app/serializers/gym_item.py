""" Serializer for Gym Item model """
from app.models.gym_item import GymItem
from app.serializers.gym import GymSerializer
from rest_framework import serializers


class GymItemSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializer for Gym Item model """

    gym = GymSerializer(read_only=True, many=False)

    class Meta:
        """ Meta Class of the Serializer """
        model = GymItem
        fields = ['id', 'gym', 'gym_visit_date']
