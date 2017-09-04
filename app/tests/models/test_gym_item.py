""" Test for Gym Model """
from django.test import TestCase
from django.db import IntegrityError
from django.contrib.auth.models import User
from app.models.profile import Profile
from app.models.gym import Gym
from app.models.gym_item import GymItem
from app.tests.common import create_gym_item

GYM_NAME = 'Test Gym'
GYM_LOCATION = 'this way, that way'
USERNAME = 'test'
LAST_VISIT_DATE = '1988-01-12'


class TestGymItemObject(TestCase):
    """
    Test the Gym Item Model
    """

    def setUp(self):
        """ Set up the test """
        super(TestGymItemObject, self).setUp()
        self.gym_item = create_gym_item(
            USERNAME,
            GYM_NAME,
            GYM_LOCATION,
            LAST_VISIT_DATE
        )

    def test_default_hidden(self):
        """
        Test the hidden flag on the created gym item object defaults to False
        """
        self.assertEqual(self.gym_item.hidden, False)

    def test_last_visit_date(self):
        """ Test the last visit date on the create gym item object """
        self.assertEqual(self.gym_item.last_visit_date, LAST_VISIT_DATE)

    def test_object_string(self):
        """ Test the string the object returns """
        self.assertEqual(
            self.gym_item.__str__(),
            '{} - {}'.format(USERNAME, GYM_NAME)
        )


class TestGymItemObjectCreation(TestCase):
    """
    Test the creation of Gym Item Model objects
    """

    def test_profile_not_defined(self):
        """ Test that exception is raised if no profile supplied """
        with self.assertRaises(IntegrityError):
            gym = Gym.objects.create(name=GYM_NAME, location=GYM_LOCATION)
            GymItem.objects.create(gym=gym)

    def test_gym_not_defined(self):
        """ Test that exception is raised if no gym supplied """
        with self.assertRaises(IntegrityError):
            user = User.objects.create(username=USERNAME)
            profile = Profile.objects.create(user=user)
            GymItem.objects.create(profile=profile)

    @staticmethod
    def test_last_visit_date_not_defined():
        """
        Test that exception is not raised if no last visit date is supplied
        """
        gym_item = create_gym_item(
            USERNAME,
            GYM_NAME,
            GYM_LOCATION,
            LAST_VISIT_DATE
        )
        gym_item.full_clean()
