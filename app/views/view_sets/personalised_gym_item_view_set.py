# pylint: disable=too-many-ancestors, invalid-name, no-self-use
""" View Set for personalised GymItem api """
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets, status
from app.models.profile import Profile
from app.models.gym_item import GymItem
from app.serializers.gym_item import GymItemSerializer
from app.views.view_sets.common import create_gym_visit


class UserGymGymItemViewSet(viewsets.GenericViewSet):
    """
    View set for the Gyms visits
    """
    serializer_class = GymItemSerializer

    def list(self, request, personalised_gyms_pk=None):
        """
        Define response for the listing of the gym's visits

        :param request: Django Request
        :param personalised_gyms_pk: ID of the Gym getting the visits for
        :return: Django Rest Framework Response
        """
        profile = Profile.objects.get(user=self.request.user)
        queryset = GymItem.objects.filter(
            profile=profile,
            gym__id=personalised_gyms_pk,
            hidden=False
        ).order_by('id')
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
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
        return create_gym_visit(request, gym_id=personalised_gyms_pk)


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
