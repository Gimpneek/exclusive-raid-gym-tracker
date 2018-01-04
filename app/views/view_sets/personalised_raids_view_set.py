# pylint: disable=too-many-ancestors
""" View Set for personalised Gym api """
from rest_framework.response import Response
from rest_framework import viewsets
from app.models.profile import Profile
from app.models.raid_item import RaidItem
from app.serializers.raid_item import RaidItemSerializer


class UserRaidsViewSet(viewsets.ViewSet):
    """
    View Set for active raids on Gyms the logged in user is following
    """
    serializer_class = RaidItemSerializer

    def list(self, request):
        """
        Define response for the listing of active raids on the user's
        tracked gyms

        :param request: Django Request
        :return: Django Rest Framework Response
        """
        profile = Profile.objects.get(user=self.request.user)
        gyms = profile.tracked_gyms.all()
        queryset = RaidItem.objects.filter(gym__in=gyms)
        serializer = RaidItemSerializer(
            queryset,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)
