""" Test the gym item view """
from datetime import datetime
from django.core.urlresolvers import reverse_lazy
from app.models.gym_item import GymItem
from app.tests.views.gym_item_common import GymViewCommonCase


class TestGymItemView(GymViewCommonCase):
    """ Gym Item view tests """

    def test_redirects_logged_out_user(self):
        """ Test that a logged out user is redirected to the Homepage """
        resp = self.client.get(
            reverse_lazy(
                'add_gym_raid',
                kwargs={
                    'gym_id': self.gym_item.id
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
                'add_gym_raid',
                kwargs={
                    'gym_id': self.gym_item.id
                }
            )
        )
        self.assertEqual(resp.templates[0].name, 'app/add_gym_raid.html')

    def test_submit_invalid_date(self):
        """
        Test that shows error on form when submitting a bad date
        """
        self.client.login(username='test', password='password')
        resp = self.client.post(
            reverse_lazy(
                'add_gym_raid',
                kwargs={
                    'gym_id': self.gym_item.id
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
                'add_gym_raid',
                kwargs={
                    'gym_id': self.gym_item.id
                }
            ),
            data={
                'last_visit_date': '1990-04-13'
            }
        )
        self.assertEqual(resp.url, reverse_lazy('gym_list'))
        gym_item = GymItem.objects.filter(gym__name='Test Gym').last()
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
                'add_gym_raid',
                kwargs={
                    'gym_id': self.gym_item.id
                }
            )
        )
        input_el = 'name="last_visit_date" type="date" value="{}"'.format(
            datetime.now().strftime('%Y-%m-%d')
        )
        self.assertTrue(input_el in str(resp.content))
