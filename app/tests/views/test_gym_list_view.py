""" Test the gym list view """
from datetime import datetime, timedelta
from django.core.urlresolvers import reverse_lazy
from app.models.gym_item import GymItem
from app.models.gym import Gym
from app.tests.views.gym_item_common import GymViewCommonCase


class TestGymListView(GymViewCommonCase):
    """ Gym List view tests """

    def test_redirects_logged_out_user(self):
        """ Test that a logged out user is redirected to the Homepage """
        resp = self.client.get(reverse_lazy('gym_list'))
        self.assertTrue(str(reverse_lazy('login')) in resp.url)

    def test_shows_gym_list(self):
        """
        Test that signed in user sees Gym List
        """
        self.client.login(username='test', password='password')
        resp = self.client.get(reverse_lazy('gym_list'))
        self.assertEqual(resp.templates[0].name, 'app/gym_list.html')

    def test_shows_visited_gyms(self):
        """
        Test that visited gyms are visible when have visited all gyms
        """
        self.client.login(username='test', password='password')
        resp = self.client.get(reverse_lazy('gym_list'))
        self.assertTrue('Visited Gyms' in str(resp.content))
        self.assertFalse('Gyms to visit' in str(resp.content))

    def test_shows_yet_to_visit_gyms(self):
        """
        Test that when visited no gyms
        """
        gym_item = GymItem.objects.get(gym__name='Test Gym')
        gym_item.last_visit_date = None
        gym_item.save()
        self.client.login(username='test', password='password')
        resp = self.client.get(reverse_lazy('gym_list'))
        self.assertTrue('Gyms to visit' in str(resp.content))
        self.assertFalse('Visited Gyms' in str(resp.content))

    def test_shows_gym_with_raid(self):
        """
        Test that when a raid is active on gym it shows it
        """
        gym_item = GymItem.objects.get(gym__name='Test Gym')
        gym_item.last_visit_date = None
        gym_item.save()
        gym = Gym.objects.get(name='Test Gym')
        gym.raid_end_date = \
            (datetime.now() + timedelta(hours=1)).strftime(
                '%Y-%m-%d %H:%M:%S+0000')
        gym.raid_level = 6
        gym.raid_pokemon = 'Test Pokemon'
        gym.save()
        self.client.login(username='test', password='password')
        resp = self.client.get(reverse_lazy('gym_list'))
        self.assertTrue('Test Pokemon (6)' in str(resp.content))
