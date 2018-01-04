# pylint: disable=too-many-ancestors
""" View Set for personalised api """
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets, status
from app.models.profile import Profile
from app.models.gym import Gym
from app.models.gym_item import GymItem
from app.serializers.gym import GymSerializer
from app.serializers.profile import ProfileSerializer
from app.serializers.gym_item import GymItemSerializer


class UserProfileViewSet(viewsets.ReadOnlyModelViewSet):
    """
    View set for the logged in user
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_queryset(self):
        """ Get the queryset """
        return Profile.objects.filter(user=self.request.user)


class UserGymViewSet(viewsets.ViewSet):
    """
    View Set for Gyms the logged in user is following
    """
    serializer_class = GymSerializer

    def list(self, request):
        """
        Define response for the listing of the user's tracked gyms

        :param request: Django Request
        :return: Django Rest Framework Response
        """
        profile = Profile.objects.get(user=self.request.user)
        queryset = profile.tracked_gyms.all()
        serializer = GymSerializer(
            queryset,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
        Define response for retrieve an individual gym

        :param request: Django Request
        :param gym_pk: ID for the Gym
        :return: Django Rest Framework Response
        """
        queryset = Gym.objects.filter(pk=pk)
        gym_visit = get_object_or_404(queryset, pk=pk)
        serializer = GymSerializer(gym_visit, context={'request': request})
        return Response(serializer.data)

    def create(self, request):
        """
        Don't allow POST request

        :param request: Django Request
        :return: http 405 code
        """
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class UserGymGymItemViewSet(viewsets.ViewSet):
    """
    View set for the Gyms visits
    """
    http_method_names = ['get']
    serializer_class = GymItemSerializer


    def list(self, request, personalised_gyms_pk=None):
        """
        Define response for the listing of the gym's visits

        :param request: Django Request
        :param pk: ID of the Gym getting the visits for
        :return: Django Rest Framework Response
        """
        profile = Profile.objects.get(user=self.request.user)
        queryset = GymItem.objects.filter(
            profile=profile,
            gym__id=personalised_gyms_pk
        )
        serializer = GymItemSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, personalised_gyms_pk=None, pk=None):
        """
        Define response for retrieve an individual visit to the gym

        :param request: Django Request
        :param personalised_gym_pk: ID for the Gym the visit is for
        :param pk: ID of the visit
        :return: Django Rest Framework Response
        """
        queryset = GymItem.objects.filter(pk=pk)
        gym_visit = get_object_or_404(queryset, pk=pk)
        serializer = GymItemSerializer(gym_visit, context={'request': request})
        return Response(serializer.data)
