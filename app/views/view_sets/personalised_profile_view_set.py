# pylint: disable=too-many-ancestors
""" View Set for personalised api """
from rest_framework import viewsets
from rest_framework.response import Response
from app.models.profile import Profile
from app.serializers.profile import ProfileSerializer


class UserProfileViewSet(viewsets.ViewSet):
    """
    View set for the logged in user
    """
    serializer_class = ProfileSerializer

    def list(self, request):
        """
        Instead of returning list return single record

        :param request: Django Request
        :return: Django Rest Framework Response
        """
        queryset = Profile.objects.get(user=self.request.user)
        serializer = ProfileSerializer(queryset)
        return Response(serializer.data)
