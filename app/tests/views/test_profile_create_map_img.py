""" Test the profile view """
from datetime import date
from django.test import TestCase
from django.contrib.auth.models import User
from app.models.profile import Profile
from app.models.gym import Gym
from app.models.gym_item import GymItem
from app.views.user_profile import create_map_img
from os import environ


USERNAME = 'test'


class TestProfileCreateMapImg(TestCase):
    """ Profile view tests """

    def setUp(self):
        """ Set up tests """
        super(TestProfileCreateMapImg, self).setUp()
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
        environ['MAPS_API_KEY'] = 'test_key'

    def test_returns_marker(self):
        """
        Test that create_map_img returns the marker in the string
        """
        map_img = create_map_img(self.raids)
        self.assertEqual(
            map_img,
            'https://maps.googleapis.com/maps/api/staticmap'
            '?center=53.7954869,-1.5460196'
            '&zoom=14'
            '&scale=2'
            '&size=600x300'
            '&maptype=roadmap'
            '&key=test_key'
            '&markers=color:red%7C1337,666'
        )
