""" Test the profile view """
from datetime import date
from django.test import TestCase
from django.contrib.auth.models import User
from app.models.profile import Profile
from app.models.gym import Gym
from app.models.gym_item import GymItem
from app.views.user_profile import get_raids_as_js


USERNAME = 'test'


class TestProfileRaidsAsJs(TestCase):
    """ Profile view tests """

    def setUp(self):
        """ Set up tests """
        super(TestProfileRaidsAsJs, self).setUp()
        user = User.objects.create(username=USERNAME)
        profile = Profile.objects.create(
            user=user,
            pokemon_go_username=USERNAME
        )
        gym = Gym.objects.create(
            name='Test Gym',
            location='1337,666'
        )
        GymItem.objects.create(
            gym=gym,
            profile=profile,
            last_visit_date= date.today()
        )
        self.raids = GymItem.objects.all()

    def test_returns_json(self):
        """
        Test that get_raids_as_js returns the marker in the string
        """
        map_js = get_raids_as_js(self.raids)
        self.assertEqual(map_js, '[{lat: 1337,lng: 666}]')
