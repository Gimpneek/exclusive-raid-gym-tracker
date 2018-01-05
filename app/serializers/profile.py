# pylint: disable=no-self-use
""" Serializer for Profile model """
from app.models.profile import Profile
from rest_framework import serializers


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializer for Profile model """

    username = serializers.SerializerMethodField()

    def get_username(self, item):
        """
        Set the raid information on the model
        :param item: Model item
        :return: raid information
        """
        return item.user.username

    class Meta:
        """ Meta Class of the Serializer """
        model = Profile
        fields = (
            'id',
            'username',
            'pokemon_go_username'
        )
