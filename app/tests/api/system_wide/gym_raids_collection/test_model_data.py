""" Test the API for Gyms """
from datetime import datetime, timedelta
from app.models.gym import Gym
from app.models.gym_item import GymItem
from app.models.raid_item import RaidItem
from app.tests.api.system_wide.gym_raids_collection\
    .gym_raids_collection_common import GymRaidsCollectionCommonCase
import pytz


class TestGymCollectionModelData(GymRaidsCollectionCommonCase):
    """ Test the API methods for the Gym """

    def test_gym_list(self):
        """
        Test that a list of Gyms is returned
        """
        RaidItem.objects.create(
            gym=self.gym,
            pokemon='Old Pokemon',
            level=5,
            end_date='1988-01-12 06:00:00+00:00'
        )
        resp = self.api.get(self.url)
        results = resp.data
        self.assertEqual(len(results), 2)

    def test_pokemon(self):
        """
        Test that the pokemon for the raid is returned
        """
        resp = self.api.get(self.url)
        results = resp.data[0]
        self.assertEqual(results.get('pokemon'), 'Test Pokemon')

    def test_level(self):
        """
        Test that the level for the raid is returned
        """
        resp = self.api.get(self.url)
        results = resp.data[0]
        self.assertEqual(results.get('level'), 5)

    def test_end_date(self):
        """
        Test that the end date for the raid is returned
        """
        resp = self.api.get(self.url)
        results = resp.data[0]
        self.assertTrue(
            self.raid_time.strftime('%Y-%m-%dT%H:%M') in results['end_date']
        )
