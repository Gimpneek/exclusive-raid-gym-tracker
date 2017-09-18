""" Test for Raid Item Model """
from django.test import TestCase
from django.db import IntegrityError
from app.models.gym import Gym
from app.models.raid_item import RaidItem
from app.tests.common import create_gym_item

GYM_NAME = 'Test Gym'
GYM_LOCATION = 'this way, that way'
USERNAME = 'test'
LAST_VISIT_DATE = '1988-01-12'
RAID_POKEMON = 'Test'
RAID_LEVEL = 5
RAID_END_DATE = '1988-01-12 06:00:00'


class TestRaidItemObject(TestCase):
    """
    Test the Gym Item Model
    """

    def setUp(self):
        """ Set up the test """
        super(TestRaidItemObject, self).setUp()
        self.gym_item = create_gym_item(
            USERNAME,
            GYM_NAME,
            GYM_LOCATION,
            LAST_VISIT_DATE
        )
        self.raid = RaidItem.objects.create(
            gym=self.gym_item.gym,
            pokemon=RAID_POKEMON,
            level=RAID_LEVEL,
            end_date=RAID_END_DATE
        )

    def test_pokemon(self):
        """
        Test the Pokemon of the raid
        """
        self.assertEqual(self.raid.pokemon, RAID_POKEMON)

    def test_level(self):
        """ Test the Level of the raid """
        self.assertEqual(self.raid.level, RAID_LEVEL)

    def test_end_date(self):
        """ Test the end date of the raid"""
        self.assertEqual(self.raid.end_date, RAID_END_DATE)

    def test_object_string(self):
        """ Test the string the object returns """
        self.assertEqual(
            self.raid.__str__(),
            '{} on {}'.format(RAID_POKEMON, GYM_NAME)
        )


class TestRaidItemObjectCreation(TestCase):
    """
    Test the creation of Raid Item Model objects
    """

    def setUp(self):
        """ Set up test """
        super(TestRaidItemObjectCreation, self).setUp()
        self.gym = Gym.objects.create(name=GYM_NAME, location=GYM_LOCATION)

    def test_level_not_defined(self):
        """ Test that no exception is raised if no level supplied """
        raid = RaidItem.objects.create(
            gym=self.gym,
            pokemon=RAID_POKEMON,
            end_date=RAID_END_DATE
        )
        raid.full_clean()

    def test_end_date_not_defined(self):
        """ Test that no exception is raised if no end_date supplied """
        raid = RaidItem.objects.create(
            gym=self.gym,
            pokemon=RAID_POKEMON,
            level=RAID_LEVEL
        )
        raid.full_clean()

    def test_gym_not_defined(self):
        """ Test that exception is raised if no gym supplied """
        with self.assertRaises(IntegrityError):
            RaidItem.objects.create(
                pokemon=RAID_POKEMON,
                level=RAID_LEVEL,
                end_date=RAID_END_DATE
            )

    def test_no_pokemon(self):
        """
        Test that exception is not raised if no pokemon is supplied
        """
        raid = RaidItem.objects.create(
            gym=self.gym,
            end_date=RAID_END_DATE,
            level=RAID_LEVEL
        )
        raid.full_clean()
