from datetime import datetime, timedelta
from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from app.models.profile import Profile
from app.models.gym import Gym
from app.models.gym_item import GymItem
from app.models.raid_item import RaidItem
import pytz


class APICommonCase(TestCase):
    """
    Set up the API for testing
    """

    def setUp(self):
        """
        Set up the tests
        """
        super(APICommonCase, self).setUp()
        User.objects.create(username='test')
        self.user = User.objects.get(username='test')
        self.user.set_password('password')
        self.user.save()
        self.profile = Profile.objects.create(
            user=self.user,
            pokemon_go_username="Gimpneek"
        )
        self.api = APIClient()
        self.api.login(username='test', password='password')
        self.create_gym()
        self.create_raid()

    def create_gym(self):
        """
        Create a Gym for use in the API tests
        """
        self.gym = Gym.objects.create(
            name='Test Gym',
            location='666,1337',
            image_url='image.jpg'
        )

    def create_raid(self):
        """
        Create a Raid for use in the API tests
        """
        self.raid_time = datetime.now(tz=pytz.UTC) + timedelta(hours=1)
        RaidItem.objects.create(
            gym=self.gym,
            pokemon='Test Pokemon',
            level=5,
            end_date=self.raid_time
        )

    def create_gym_visit(self):
        """
        Create a gym visit for the API tests
        """
        self.gym_visit = GymItem.objects.create(
            gym=self.gym,
            profile=self.profile,
            gym_visit_date=self.visit_date
        )

    def get_gym_visit_count(self):
        """
        Get the count of the GymItems in the system

        :return: count of GymItems
        :rtype: int
        """
        return GymItem.objects.all().count()
