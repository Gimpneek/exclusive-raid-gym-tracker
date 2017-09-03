""" Test for Gym Model """
from django.test import TestCase
from django.core.exceptions import ValidationError
from app.models.gym import Gym


GYM_NAME = 'Test Gym'
GYM_LOCATION = 'this way, that way'
GYM_IMAGE = 'http://www.test.com/image.png'
GYM_ID = '0123456789'


class TestGymObject(TestCase):
    """
    Test the Gym Model
    """

    def setUp(self):
        """ Set up the test """
        super(TestGymObject, self).setUp()
        self.gym = Gym.objects.create(
            name=GYM_NAME,
            location=GYM_LOCATION,
            image_url=GYM_IMAGE,
            gym_hunter_id=GYM_ID
        )

    def test_gym_name(self):
        """ Test the name on the created gym object """
        self.assertEqual(self.gym.name, GYM_NAME)

    def test_gym_location(self):
        """ Test the location on the created gym object """
        self.assertEqual(self.gym.location, GYM_LOCATION)

    def test_gym_image_url(self):
        """ Test the image url on the created gym object """
        self.assertEqual(self.gym.image_url, GYM_IMAGE)

    def test_gym_hunter_id(self):
        """ Test the Gym Hunter ID on the created gym object """
        self.assertEqual(self.gym.gym_hunter_id, GYM_ID)

    def test_object_string(self):
        """ Test the string the object returns """
        self.assertEqual(self.gym.__str__(), GYM_NAME)


class TestGymObjectCreation(TestCase):
    """
    Test the creation of Gym Model objects
    """

    def test_raises_if_name_not_defined(self):
        """ Test that exception is raised if no gym name supplied """
        with self.assertRaises(ValidationError):
            gym = Gym.objects.create(
                location=GYM_LOCATION,
                image_url=GYM_IMAGE,
                gym_hunter_id=GYM_ID
            )
            gym.full_clean()

    def test_raises_if_location_not_defined(self):
        """ Test that exception is raised if no gym location supplied """
        with self.assertRaises(ValidationError):
            gym = Gym.objects.create(
                name=GYM_NAME,
                image_url=GYM_IMAGE,
                gym_hunter_id=GYM_ID
            )
            gym.full_clean()

    def test_doesnt_raise_if_gym_hunter_id_not_defined(self):
        """ Test that exception is not raised if no gym hunter id supplied """
        gym = Gym.objects.create(
            name=GYM_NAME,
            location=GYM_LOCATION,
            image_url=GYM_IMAGE
        )
        gym.full_clean()

    def test_doesnt_raise_if_image_not_defined(self):
        """ Test that exception is not raised if no image url is suppled """
        gym = Gym.objects.create(
            name=GYM_NAME,
            location=GYM_LOCATION,
            gym_hunter_id=GYM_ID
        )
        gym.full_clean()