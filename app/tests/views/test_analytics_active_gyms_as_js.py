""" Test the profile view """
from datetime import datetime
from django.test import TestCase
from app.models.gym import Gym
from app.models.raid_item import RaidItem
from app.views.analytics_dashboard import get_active_gyms_as_js


USERNAME = 'test'


class TestProfileRaidsAsJs(TestCase):
    """ Profile view tests """

    def setUp(self):
        """ Set up tests """
        super(TestProfileRaidsAsJs, self).setUp()
        gym = Gym.objects.create(
            name='Test Gym',
            location='1337,666'
        )
        RaidItem.objects.create(
            gym=gym,
            pokemon='Test',
            level=5,
            end_date=datetime.now()
        )
        self.raids = RaidItem.objects.all()

    def test_returns_json(self):
        """
        Test that get_raids_as_js returns the marker in the string
        """
        gyms = [('Test Gym', 1)]
        map_js = get_active_gyms_as_js(gyms, self.raids)
        self.assertEqual(map_js, '[{lat: 1337,lng: 666}]')
