""" Test for EX-Raid Pokemon Model """
from django.test import TestCase
from django.core.exceptions import ValidationError
from app.models.ex_raid_pokemon import ExRaidPokemon

POKEMON = 'Mewtwo'


class TestExRaidPokemonObject(TestCase):
    """
    Test the EX-Raid Pokemon Model
    """

    def setUp(self):
        """ Set up the test """
        super(TestExRaidPokemonObject, self).setUp()
        self.ex_raid_pokemon = ExRaidPokemon.objects.create(name=POKEMON)

    def test_name(self):
        """ Test the name on the created EX-Raid Pokemon object """
        self.assertEqual(self.ex_raid_pokemon.name, POKEMON)

    def test_object_string(self):
        """ Test the string the object returns """
        self.assertEqual(self.ex_raid_pokemon.__str__(), POKEMON)


class TestExRaidPokemonObjectCreation(TestCase):
    """
    Test the creation of EX-Raid Pokemon Model objects
    """

    def test_name_not_defined(self):
        """
        Test that exception is raised if no EX-Raid Pokemon name supplied
        """
        with self.assertRaises(ValidationError):
            ex_raid = ExRaidPokemon.objects.create()
            ex_raid.full_clean()
