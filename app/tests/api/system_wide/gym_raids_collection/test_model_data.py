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

    def test_raid_list(self):
        """
        Test that a list of Gyms is returned
        """
        self.assertTrue(False)

    def test_raid_pokemon(self):
        """
        Test that the name of the pokemon the raid was for is returned
        """
        self.assertTrue(False)

    def test_raid_level(self):
        """
        Test that the level of the raid is returned
        """
        self.assertTrue(False)

    def test_raid_end_date(self):
        """
        Test that the end date of the raid is returned`
        """
        self.assertTrue(False)
