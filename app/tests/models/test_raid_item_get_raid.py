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
RAID_END_DATE = '1988-01-12 06:00:00'


class TestRaidItemGetRaid(TestCase):
    """
    Test the RaidItem Model's get_raid method
    """

    def setUp(self):
        """ Set up the test """
        super(TestRaidItemGetRaid, self).setUp()
        gym = Gym.objects.create(
            name=GYM_NAME,
            location=GYM_LOCATION,
            image_url=GYM_IMAGE,
            gym_hunter_id=GYM_ID
        )
        raid = RaidItem.objects.create(
            pokemon=RAID_POKEMON,
            level=RAID_LEVEL,
            end_date=RAID_END_DATE,
            gym=gym
        )
        self.gym = Gym.objects.get(pk=gym.id)
        self.raid = RaidItem.objects.get(pk=raid.id)

    def test_raid_in_future(self):
        """
        Test get_raid returns the raid dictionary if the
        raid is in the future
        """
        starting_dt = datetime(1988, 1, 12, 5, 0, 0)
        raid_data = self.raid.get_raid(starting_dt)
        self.assertEqual(raid_data.get('pokemon'), RAID_POKEMON)
        self.assertEqual(raid_data.get('level'), RAID_LEVEL)
        self.assertEqual(raid_data.get('time_left'), '1:00:00 remaining')

    def test_raid_in_past(self):
        """
        Test get_raid returns None if the raid is in the past
        """
        starting_dt = datetime(1988, 1, 12, 6, 0, 1)
        raid_data = self.raid.get_raid(starting_dt)
        self.assertFalse(raid_data)

    def test_no_raid_pokemon(self):
        """
        Test that if there's no raid pokemon then 'Egg' is returned
        """
        starting_dt = datetime(1988, 1, 12, 5, 0, 0)
        raid = RaidItem.objects.create(
            gym=self.gym,
            level=RAID_LEVEL,
            end_date=RAID_END_DATE
        )
        raid_instance = RaidItem.objects.get(pk=raid.id)
        self.assertEqual(
            raid_instance.get_raid(starting_dt).get('pokemon'),
            'Egg'
        )

    def test_raid_pokemon(self):
        """
        Test that when raid pokemon has a name that it's name is returned
        """
        starting_dt = datetime(1988, 1, 12, 5, 0, 0)
        raid = RaidItem.objects.create(
            gym=self.gym,
            pokemon=RAID_POKEMON,
            level=RAID_LEVEL,
            end_date=RAID_END_DATE
        )
        raid_instance = RaidItem.objects.get(pk=raid.id)
        self.assertEqual(
            raid_instance.get_raid(starting_dt).get('pokemon'),
            RAID_POKEMON
        )

    def test_no_raid_level(self):
        """
        Test that if there's no raid level then None is returned
        """
        starting_dt = datetime(1988, 1, 12, 5, 0, 0)
        raid = RaidItem.objects.create(
            gym=self.gym,
            pokemon=RAID_POKEMON,
            end_date=RAID_END_DATE
        )
        raid_instance = RaidItem.objects.get(pk=raid.id)
        self.assertFalse(raid_instance.get_raid(starting_dt))

    def test_no_raid_end_date(self):
        """
        Test that if there's no raid end date then None is returned
        """
        starting_dt = datetime(1988, 1, 12, 5, 0, 0)
        raid = RaidItem.objects.create(
            gym=self.gym,
            level=RAID_LEVEL,
            pokemon=RAID_POKEMON
        )
        raid_instance = RaidItem.objects.get(pk=raid.id)
        self.assertFalse(raid_instance.get_raid(starting_dt))

    def test_no_starting_date(self):
        """
        Test if there's no defined starting date then it uses datetime.now()
        """
        raid = RaidItem.objects.create(
            gym=self.gym,
            level=RAID_LEVEL,
            pokemon=RAID_POKEMON,
            end_date=RAID_END_DATE
        )
        raid_instance = RaidItem.objects.get(pk=raid.id)
        self.assertFalse(raid_instance.get_raid())
