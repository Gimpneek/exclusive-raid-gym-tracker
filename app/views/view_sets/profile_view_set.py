# pylint: disable=too-many-ancestors
""" View Set for Profile Serializer """
from rest_framework import viewsets
from app.models.profile import Profile
from app.serializers.profile import ProfileSerializer


class ProfileViewSet(viewsets.ReadOnlyModelViewSet):
    """
    View Set for Profile Serializer
    """

    queryset = Profile.objects.all().order_by('id')
    serializer_class = ProfileSerializer
