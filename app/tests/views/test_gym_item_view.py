""" Test the gym item view """
from django.test import TestCase
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from app.tests.common import create_gym_item
from app.models.gym_item import GymItem
from datetime import datetime


class TestGymItemView(TestCase):
    """ Gym Item view tests """

    def setUp(self):
        """ Set up User for testing """
        super(TestGymItemView, self).setUp()
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
                'gym_item',
                kwargs={
                    'gym_item_id': self.gym_item.id
                }
            )
        )
        self.assertTrue(str(reverse_lazy('login')) in resp.url)

    def test_shows_gym_item(self):
        """
        Test that signed in user sees Gym Item
        """
        self.client.login(username='test', password='password')
        resp = self.client.get(
            reverse_lazy(
                'gym_item',
                kwargs={
                    'gym_item_id': self.gym_item.id
                }
            )
        )
        self.assertEqual(resp.templates[0].name, 'app/gym_item.html')

    def test_redirects_not_users_item(self):
        """
        Test that redirects to Gym List if Gym Item doesn't belong to the user
        """
        self.client.login(username='test', password='password')
        resp = self.client.get(
            reverse_lazy(
                'gym_item',
                kwargs={
                    'gym_item_id': self.other_gym_item.id
                }
            )
        )
        self.assertEqual(resp.url, reverse_lazy('gym_list'))

    def test_submit_invalid_date(self):
        """
        Test that shows error on form when submitting a bad date
        """
        self.client.login(username='test', password='password')
        resp = self.client.post(
            reverse_lazy(
                'gym_item',
                kwargs={
                    'gym_item_id': self.gym_item.id
                }
            ),
            data={
                'last_visit_date': 'bad_string'
            }
        )
        self.assertTrue('Invalid date entered' in str(resp.content))

    def test_changes_submitted_date(self):
        """
        Test that on submitting a valid date it updates the gym_item
        """
        self.client.login(username='test', password='password')
        resp = self.client.post(
            reverse_lazy(
                'gym_item',
                kwargs={
                    'gym_item_id': self.gym_item.id
                }
            ),
            data={
                'last_visit_date': '1990-04-13'
            }
        )
        self.assertEqual(resp.url, reverse_lazy('gym_list'))
        gym_item = GymItem.objects.get(gym__name='Test Gym')
        self.assertEqual(
            gym_item.last_visit_date.strftime('%Y-%m-%d'), '1990-04-13')

    def test_no_date_set(self):
        """
        Test that when no date is set on gym item it shows an empty input
        """
        self.gym_item.last_visit_date = None
        self.gym_item.save()
        self.client.login(username='test', password='password')
        resp = self.client.get(
            reverse_lazy(
                'gym_item',
                kwargs={
                    'gym_item_id': self.gym_item.id
                }
            )
        )
        input_el = 'name="last_visit_date" type="date" value="{}"'.format(
            datetime.now().strftime('%Y-%m-%d')
        )
        self.assertTrue(input_el in str(resp.content))
