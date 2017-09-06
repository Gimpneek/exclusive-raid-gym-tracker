""" Test for Gym Model """
from datetime import datetime, tzinfo
from django.test import TestCase
from app.models.gym import Gym
import pytz


GYM_NAME = 'Test Gym'
GYM_LOCATION = 'this way, that way'
GYM_IMAGE = 'http://www.test.com/image.png'
GYM_ID = '0123456789'
RAID_POKEMON = 'Mewtwo'
RAID_LEVEL = 5
RAID_END_DATE = '1988-01-12 06:00:00+0000'


class TestGymObject(TestCase):
    """
    Test the Gym Model
    """

    def setUp(self):
        """ Set up the test """
        super(TestGymObject, self).setUp()
        gym = Gym.objects.create(
            name=GYM_NAME,
            location=GYM_LOCATION,
            image_url=GYM_IMAGE,
            gym_hunter_id=GYM_ID,
            raid_pokemon=RAID_POKEMON,
            raid_level=RAID_LEVEL,
            raid_end_date=RAID_END_DATE
        )
        self.gym = Gym.objects.get(pk=gym.id)

    def test_raid_in_future(self):
        """
        Test get_raid_information returns the raid dictionary if the
        raid is in the future
        """
        starting_dt = datetime(1988, 1, 12, 5, 0, 0, tzinfo=pytz.utc)
        raid_data = self.gym.get_raid_information(starting_dt)
        self.assertEqual(raid_data.get('pokemon'), RAID_POKEMON)
        self.assertEqual(raid_data.get('level'), RAID_LEVEL)
        self.assertEqual(raid_data.get('time_left'), '1:00:00 remaining')

    def test_raid_in_past(self):
        """
        Test get_raid_information returns None if the raid is in the past
        """
        starting_dt = datetime(1988, 1, 12, 6, 0, 1, tzinfo=pytz.utc)
        raid_data = self.gym.get_raid_information(starting_dt)
        self.assertIsNone(raid_data)

    def test_no_raid_pokemon(self):
        """
        Test that if there's no raid pokemon then None is returned
        """
        starting_dt = datetime(1988, 1, 12, 6, 0, 1, tzinfo=pytz.utc)
        gym = Gym.objects.create(
            name=GYM_NAME,
            location=GYM_LOCATION,
            image_url=GYM_IMAGE,
            gym_hunter_id=GYM_ID,
            raid_level=RAID_LEVEL,
            raid_end_date=RAID_END_DATE
        )
        gym_instance = Gym.objects.get(pk=gym.id)
        self.assertIsNone(gym_instance.get_raid_information(starting_dt))

    def test_no_raid_level(self):
        """
        Test that if there's no raid level then None is returned
        """
        starting_dt = datetime(1988, 1, 12, 6, 0, 1, tzinfo=pytz.utc)
        gym = Gym.objects.create(
            name=GYM_NAME,
            location=GYM_LOCATION,
            image_url=GYM_IMAGE,
            gym_hunter_id=GYM_ID,
            raid_pokemon=RAID_POKEMON,
            raid_end_date=RAID_END_DATE
        )
        gym_instance = Gym.objects.get(pk=gym.id)
        self.assertIsNone(gym_instance.get_raid_information(starting_dt))

    def test_no_raid_end_date(self):
        """
        Test that if there's no raid end date then None is returned
        """
        starting_dt = datetime(1988, 1, 12, 6, 0, 1, tzinfo=pytz.utc)
        gym = Gym.objects.create(
            name=GYM_NAME,
            location=GYM_LOCATION,
            image_url=GYM_IMAGE,
            gym_hunter_id=GYM_ID,
            raid_level=RAID_LEVEL,
            raid_pokemon=RAID_POKEMON
        )
        gym_instance = Gym.objects.get(pk=gym.id)
        self.assertIsNone(gym_instance.get_raid_information(starting_dt))

    def test_no_starting_date(self):
        """
        Test if there's no defined starting date then it uses datetime.now()
        """
        gym = Gym.objects.create(
            name=GYM_NAME,
            location=GYM_LOCATION,
            image_url=GYM_IMAGE,
            gym_hunter_id=GYM_ID,
            raid_level=RAID_LEVEL,
            raid_pokemon=RAID_POKEMON,
            raid_end_date=RAID_END_DATE
        )
        gym_instance = Gym.objects.get(pk=gym.id)
        self.assertIsNone(gym_instance.get_raid_information())
