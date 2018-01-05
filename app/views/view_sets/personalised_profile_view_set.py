# pylint: disable=too-many-ancestors
""" View Set for personalised api """
from rest_framework import viewsets
from rest_framework.response import Response
from app.models.profile import Profile
from app.serializers.profile import ProfileSerializer


class UserProfileViewSet(viewsets.GenericViewSet):
    """
    View set for the logged in user
    """
    serializer_class = ProfileSerializer

    def get_queryset(self):
        """ Get the queryset for the API call """
        return Profile.objects.filter(user=self.request.user).order_by('id')

    def list(self, request):
        """
        Instead of returning list return single record

        :param request: Django Request
        :return: Django Rest Framework Response
        """
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = ProfileSerializer(queryset)
        return Response(serializer.data)
