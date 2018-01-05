# pylint: disable=too-many-ancestors
""" View Set for Gym Item Serializer """
from rest_framework import viewsets
from app.models.gym_item import GymItem
from app.serializers.gym_item import GymItemSerializer
from app.views.view_sets.common import create_gym_visit


class GymItemViewSet(viewsets.ModelViewSet):
    """
    View Set for Gym Item Serializer
    """
    queryset = GymItem.objects.all()
    serializer_class = GymItemSerializer

    def get_queryset(self):
        """
        Get the query set to return for Gym Item API
        :return: List of GymItem instances for user
        """
        return GymItem.objects.filter(profile__user=self.request.user)\
            .order_by('gym_visit_date')

    def create(self, request, *args, **kwargs):
        """
        Create a new Gym Visit
        :param request: Request sent to endpoint
        :return: Success code
        """
        return create_gym_visit(request)
