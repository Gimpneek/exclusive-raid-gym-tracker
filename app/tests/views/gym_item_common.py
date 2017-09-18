""" Test the common parts of the gym item view """
from django.test import TestCase
from django.contrib.auth.models import User
from app.tests.common import create_gym_item
from app.models.gym_item import GymItem


class GymViewCommonCase(TestCase):
    """ Hide Gym Item view tests """

    def setUp(self):
        """ Set up User for testing """
        super(GymViewCommonCase, self).setUp()
        create_gym_item(
            'test', 'Test Gym', 'Test Location', '1988-01-12 06:00:00')
        self.user = User.objects.get(username='test')
        self.gym_item = GymItem.objects.get(gym__name='Test Gym')
        self.user.set_password('password')
        self.user.save()
