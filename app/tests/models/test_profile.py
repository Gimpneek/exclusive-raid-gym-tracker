""" Test for Profile Model """
from django.test import TestCase
from django.db import IntegrityError
from django.contrib.auth.models import User
from app.models.profile import Profile


USERNAME = 'test'


class TestProfileObject(TestCase):
    """
    Test the Profile Model
    """

    def setUp(self):
        """ Set up the test """
        super(TestProfileObject, self).setUp()
        self.user = User.objects.create(username=USERNAME)
        self.profile = Profile.objects.create(
            user=self.user,
            pokemon_go_username=USERNAME
        )

    def test_pogo_username(self):
        """ Test the pogo username on the created profile object """
        self.assertEqual(self.profile.pokemon_go_username, USERNAME)

    def test_object_string(self):
        """ Test the string the object returns """
        self.assertEqual(self.profile.__str__(), self.user.username)


class TestProfileObjectCreation(TestCase):
    """
    Test the creation of Profile Model objects
    """

    def test_raises_if_user_not_defined(self):
        """ Test that exception is raised if no user supplied """
        with self.assertRaises(IntegrityError):
            Profile.objects.create(pokemon_go_username=USERNAME)

    def test_doesnt_raise_if_pogo_name_not_defined(self):
        """
        Test that exception is not raised if no pokemon go username supplied
        """
        user = User.objects.create(username=USERNAME)
        profile = Profile.objects.create(user=user)
        profile.full_clean()
