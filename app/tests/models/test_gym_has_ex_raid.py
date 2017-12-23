""" Test had_ex_raid on Gym Model """
from django.test import TestCase
from app.models.gym import Gym
from app.models.raid_item import RaidItem
from app.models.ex_raid_pokemon import ExRaidPokemon


GYM_NAME = 'Test Gym'
GYM_LOCATION = 'this way, that way'
GYM_IMAGE = 'http://www.test.com/image.png'
GYM_ID = '0123456789'
RAID_POKEMON = 'Mewtwo'
RAID_LEVEL = 5
RAID_END_DATE = '1988-01-12 06:00:00+00:00'


class TestGymHadExRaid(TestCase):
    """
    Test the Gym Model's had_ex_raid method
    """

    def setUp(self):
        """ Set up the test """
        super(TestGymHadExRaid, self).setUp()
        ExRaidPokemon.objects.create(name=RAID_POKEMON)
        gym = Gym.objects.create(
            name=GYM_NAME,
            location=GYM_LOCATION,
            image_url=GYM_IMAGE,
            gym_hunter_id=GYM_ID
        )
        self.gym = Gym.objects.get(pk=gym.id)

    def test_no_ex_raid(self):
        """
        Test that had_ex_raid returns False if no EX-Raids happened on
        the Gym
        """
        RaidItem.objects.create(
            pokemon='Articuno',
            level=RAID_LEVEL,
            end_date=RAID_END_DATE,
            gym=self.gym
        )
        self.assertFalse(self.gym.had_ex_raid)

    def test_had_ex_raid(self):
        """
        Test that had_ex_raid returns True if an EX-Raid has happened
        on the Gym
        """
        RaidItem.objects.create(
            pokemon=RAID_POKEMON,
            level=RAID_LEVEL,
            end_date=RAID_END_DATE,
            gym=self.gym
        )
        self.assertTrue(self.gym.had_ex_raid)
