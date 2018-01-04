# pylint: disable=too-many-ancestors, no-self-use
""" View Set for personalised Gym api """
from rest_framework.response import Response
from rest_framework import viewsets
from app.models.raid_item import RaidItem
from app.serializers.raid_item import RaidItemSerializer


class GymRaidsViewSet(viewsets.ViewSet):
    """
    View Set for active raids on Gyms the logged in user is following
    """
    serializer_class = RaidItemSerializer

    def list(self, request, system_gyms_pk=None):
        """
        Define response for the listing of active raids on the user's
        tracked gyms

        :param request: Django Request
        :param system_gyms_pk: ID of the Gym to get raids of
        :return: Django Rest Framework Response
        """
        queryset = RaidItem.objects.filter(gym__id=system_gyms_pk)
        serializer = RaidItemSerializer(
            queryset,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)
