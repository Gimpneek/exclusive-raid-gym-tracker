# pylint: disable=no-self-use
""" Serializer for Gym model """
from app.models.gym import Gym
from app.models.gym_item import GymItem
from app.models.profile import Profile
from rest_framework import serializers


class GymSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializer for Gym model """

    # Replace this with a RaidItemSerializer or something
    raid = serializers.SerializerMethodField('raid_information')
    gym_visit_date = serializers.SerializerMethodField('get_visit')

    def raid_information(self, item):
        """
        Set the raid information on the model
        :param item: Model item
        :return: raid information
        """
        return item.get_raid_information()

    def get_visit(self, item):
        """
        Get the last visit date for this gym
        :param item: Gym Item
        :return: Date of last visit
        """
        user_id = self.context.get('request').user.id
        if user_id:
            profile = Profile.objects.get(pk=user_id)
            gym_visit = GymItem.objects.filter(gym=item, profile=profile)\
                .order_by('gym_visit_date').last()
            if gym_visit:
                return gym_visit.gym_visit_date
        return None

    class Meta:
        model = Gym
        fields = (
            'id',
            'name',
            'location',
            'image_url',
            'raid',
            'gym_visit_date'
        )
