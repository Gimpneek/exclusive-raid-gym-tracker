""" Test the get_last_raid template tag """
from django.test import TestCase
from django.contrib.auth.models import User
from app.tests.common import create_gym_item
from app.models.gym import Gym
from app.templatetags.tracker_tags import get_last_raid


class TestGetLastRaid(TestCase):
    """ Test get_last_raid template tag """

    def setUp(self):
        """ Set up the tests """
        super(TestGetLastRaid, self).setUp()
        create_gym_item(
            'test', 'Test Gym', 'Test Location', '1988-01-12 06:00:00')
        self.user = User.objects.get(username='test')
        self.gym = Gym.objects.get(name='Test Gym')

    def test_last_raid_date(self):
        """
        Test that the last raid date of the gym item is returned
        """
        last_raid = get_last_raid(self.gym.id, self.user.id)
        self.assertEqual(last_raid.strftime('%Y-%m-%d'), '1988-01-12')

    def test_no_last_raid(self):
        """
        Test that if no last raid is found then None is returned
        """
        self.assertIsNone(get_last_raid(666, self.user.id))
