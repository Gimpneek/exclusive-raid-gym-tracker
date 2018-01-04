# pylint: disable=too-many-ancestors
""" View Set for personalised Gym api """
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets, status, mixins
from app.models.profile import Profile
from app.models.gym import Gym
from app.serializers.gym import GymSerializer


class UserGymViewSet(viewsets.ViewSet):
    """
    View Set for Gyms the logged in user is following
    """
    serializer_class = GymSerializer
    http_method_names = ('get', 'post', 'delete')

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

    def destroy(self, request, pk=None):
        """
        Define response to stop tracking a Gym

        :param request: Django Request
        :param pk: ID of the Gym to stop tracking
        :return: Django Rest Framework Response
        """
        profile = Profile.objects.get(user=self.request.user)
        gym = Gym.objects.get(id=pk)
        profile.tracked_gyms.remove(gym)
        profile.save()
        return Response(status=status.HTTP_301_MOVED_PERMANENTLY)

    def create(self, request):
        """
        Define response to start tracking a Gym

        :param request: Django Request
        :return: Django Rest Framework Response
        """
        gym_id = request.data.get('gym_id')
        if gym_id:
            profile = Profile.objects.get(user=self.request.user)
            gym = Gym.objects.get(id=int(gym_id))
            profile.tracked_gyms.add(gym)
            profile.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
