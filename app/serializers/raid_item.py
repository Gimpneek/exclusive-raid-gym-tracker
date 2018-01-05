""" Serializer for Raid Item model """
from app.models.raid_item import RaidItem
from app.serializers.gym import GymSerializer
from rest_framework import serializers


class RaidItemSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializer for Raid Item model """

    gym = GymSerializer(read_only=True, many=False)

    class Meta:
        """ Meta Class of the Serializer """
        model = RaidItem
        fields = ['id', 'gym', 'pokemon', 'level', 'end_date']
