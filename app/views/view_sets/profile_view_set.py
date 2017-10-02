# pylint: disable=too-many-ancestors
""" View Set for Profile Serializer """
from rest_framework import viewsets
from app.models.profile import Profile
from app.serializers.profile import ProfileSerializer


class ProfileViewSet(viewsets.ReadOnlyModelViewSet):
    """
    View Set for Profile Serializer
    """

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_queryset(self):
        """ Get the queryset """
        return Profile.objects.filter(user__id=self.request.user.id)
