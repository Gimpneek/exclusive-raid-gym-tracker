""" Test the reset gym item view """
from django.test import TestCase
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from app.tests.common import create_gym_item
from app.models.gym_item import GymItem


class TestResetGymItemView(TestCase):
    """ Reset Gym Item view tests """

    def setUp(self):
        """ Set up User for testing """
        super(TestResetGymItemView, self).setUp()
        create_gym_item('test', 'Test Gym', 'Test Location', '1988-01-12')
        create_gym_item(
            'new_user', 'Test Gym 1', 'Test Location', '1988-01-12')
        self.user = User.objects.get(username='test')
        self.gym_item = GymItem.objects.get(gym__name='Test Gym')
        self.other_gym_item = GymItem.objects.get(gym__name='Test Gym 1')
        self.user.set_password('password')
        self.user.save()

    def test_redirects_logged_out_user(self):
        """ Test that a logged out user is redirected to the Homepage """
        resp = self.client.get(
            reverse_lazy(
                'reset_gym_item',
                kwargs={
                    'gym_item_id': self.gym_item.id
                }
            )
        )
        self.assertTrue(str(reverse_lazy('login')) in resp.url)

    def test_resets_gym_item(self):
        """
        Test that sign in user will reset the Gym Item and be shown gym list
        """
        self.client.login(username='test', password='password')
        resp = self.client.get(
            reverse_lazy(
                'reset_gym_item',
                kwargs={
                    'gym_item_id': self.gym_item.id
                }
            )
        )
        self.assertEqual(resp.url, reverse_lazy('gym_list'))
        gym_item = GymItem.objects.get(gym__name='Test Gym')
        self.assertIsNone(gym_item.last_visit_date)

    def test_redirects_not_users_item(self):
        """
        Test that redirects to Gym List if Gym Item doesn't belong to the user
        """
        self.client.login(username='test', password='password')
        resp = self.client.get(
            reverse_lazy(
                'reset_gym_item',
                kwargs={
                    'gym_item_id': self.other_gym_item.id
                }
            )
        )
        self.assertEqual(resp.url, reverse_lazy('gym_list'))
        gym_item = GymItem.objects.get(gym__name='Test Gym 1')
        self.assertIsNotNone(gym_item.last_visit_date)
