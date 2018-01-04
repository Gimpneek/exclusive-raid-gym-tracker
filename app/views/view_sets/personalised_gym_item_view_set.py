# pylint: disable=too-many-ancestors, invalid-name, no-self-use
""" View Set for personalised GymItem api """
from datetime import datetime
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets, status
from app.models.profile import Profile
from app.models.gym import Gym
from app.models.gym_item import GymItem
from app.serializers.gym_item import GymItemSerializer
import pytz


class UserGymGymItemViewSet(viewsets.ViewSet):
    """
    View set for the Gyms visits
    """
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
            gym__id=personalised_gyms_pk,
            hidden=False
        )
        serializer = GymItemSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, personalised_gyms_pk=None, pk=None):
        """
        Define response for retrieve an individual visit to the gym

        :param request: Django Request
        :param personalised_gyms_pk: ID for the Gym the visit is for
        :param pk: ID of the visit
        :return: Django Rest Framework Response
        """
        queryset = GymItem.objects.filter(pk=pk, hidden=False)
        gym_visit = get_object_or_404(queryset, pk=pk)
        serializer = GymItemSerializer(gym_visit, context={'request': request})
        return Response(serializer.data)

    def destroy(self, request, personalised_gyms_pk=None, pk=None):
        """
        Define response for deleting a visit to the defined gym

        :param request: Django Request
        :param personalised_gyms_pk: ID for the Gym
        :param pk: ID of the visit
        :return: Django Rest Framework Response
        """
        item = GymItem.objects.get(id=pk)
        item.hidden = True
        item.save()
        return Response(status=status.HTTP_301_MOVED_PERMANENTLY)

    def create(self, request, personalised_gyms_pk=None):
        """
        Define response for creating a new visit to the defined gym

        :param request: Django Request
        :param personalised_gyms_pk: ID for the Gym
        :return: Django Rest Framework Response
        """
        profile = Profile.objects.get(user=self.request.user)
        gym = Gym.objects.get(id=personalised_gyms_pk)
        try:
            gym_visit_date = datetime.strptime(
                request.data.get('gym_visit_date'),
                '%Y-%m-%dT%H:%M'
            ).replace(tzinfo=pytz.timezone('Europe/London'))
            GymItem.objects.create(
                gym=gym,
                profile=profile,
                gym_visit_date=gym_visit_date
            )
            if gym not in profile.tracked_gyms.all():
                profile.tracked_gyms.add(gym)
                profile.save()
            return Response(status=status.HTTP_201_CREATED)
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UserGymItemViewSet(viewsets.ViewSet):
    """
    View set for the Gyms visits
    """
    serializer_class = GymItemSerializer

    def list(self, request):
        """
        Define response for the listing of the gym's visits

        :param request: Django Request
        :return: Django Rest Framework Response
        """
        profile = Profile.objects.get(user=self.request.user)
        queryset = GymItem.objects.filter(
            profile=profile,
            hidden=False
        )
        serializer = GymItemSerializer(queryset, many=True)
        return Response(serializer.data)
