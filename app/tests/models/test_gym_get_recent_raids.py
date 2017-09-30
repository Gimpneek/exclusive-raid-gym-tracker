""" Test get_raid on RaidItem Model """
from datetime import datetime
from django.test import TestCase
from app.models.gym import Gym
from app.models.raid_item import RaidItem
import pytz


GYM_NAME = 'Test Gym'
GYM_LOCATION = 'this way, that way'
GYM_IMAGE = 'http://www.test.com/image.png'
GYM_ID = '0123456789'
RAID_POKEMON = 'Mewtwo'
RAID_LEVEL = 5
RAID_END_DATE = '1988-01-12 06:00:00+00:00'


class TestGymGetRecentRaids(TestCase):
    """
    Test the RaidItem Model's get_raid method
    """

    def setUp(self):
        """ Set up the test """
        super(TestGymGetRecentRaids, self).setUp()
        gym = Gym.objects.create(
            name=GYM_NAME,
            location=GYM_LOCATION,
            image_url=GYM_IMAGE,
            gym_hunter_id=GYM_ID
        )
        self.gym = Gym.objects.get(pk=gym.id)

    def test_no_gyms(self):
        """
        Test that get_recent_raids returns [] if no recent raids
        """
        raids = self.gym.get_recent_raids()
        self.assertFalse(raids)

    def test_one_raid(self):
        """
        Test that get_recent_raids returns 1 raid if 1 recent raid
        """
        RaidItem.objects.create(
            pokemon=RAID_POKEMON,
            level=RAID_LEVEL,
            end_date=RAID_END_DATE,
            gym=self.gym
        )
        raids = self.gym.get_recent_raids()
        self.assertTrue(len(raids) == 1)
        self.assertEqual(raids[0].pokemon, RAID_POKEMON)

    def test_count(self):
        """
        Test that get_recent_raids returns the number of items supplied by
        count
        """
        for i in range(0, 10):
            RaidItem.objects.create(
                pokemon=RAID_POKEMON,
                level=RAID_LEVEL,
                end_date='1988-01-12 0{}:00:00+00:00'.format(i),
                gym=self.gym
            )
        raids = self.gym.get_recent_raids(7)
        self.assertTrue(len(raids) == 7)

    def test_default_count(self):
        """
        Test that get_recent_raids returns the number of items supplied by
        count
        """
        for i in range(0, 10):
            RaidItem.objects.create(
                pokemon=RAID_POKEMON,
                level=RAID_LEVEL,
                end_date='1988-01-12 0{}:00:00+00:00'.format(i),
                gym=self.gym
            )
        raids = self.gym.get_recent_raids()
        self.assertTrue(len(raids) == 5)

    def test_bad_count_param(self):
        """
        Test that error is raises when passing a non-int count
        """
        with self.assertRaises(ValueError):
            self.gym.get_recent_raids('badness')
