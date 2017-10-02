# pylint: disable=too-many-ancestors
""" View Set for Gym Item Serializer """
from rest_framework import viewsets, response
from app.models.gym_item import GymItem
from app.models.gym import Gym
from app.models.profile import Profile
from app.serializers.gym_item import GymItemSerializer
from app.forms.gym_item import GymItemForm
import pytz


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
        form = GymItemForm(request.data)
        if form.is_valid():
            gym_visit_date = form.cleaned_data.get('gym_visit_date')\
                .replace(tzinfo=pytz.timezone('Europe/London'))
            profile = Profile.objects.get(user=request.user.id)
            gym = Gym.objects.get(pk=form.data.get('gym'))
            GymItem.objects.create(
                gym=gym,
                profile=profile,
                gym_visit_date=gym_visit_date
            )
            return response.Response(status=201)
        return response.Response(status=400)
