""" Test the gym list view """
from datetime import datetime, timedelta
from django.urls import reverse_lazy
from app.models.gym_item import GymItem
from app.models.gym import Gym
from app.models.raid_item import RaidItem
from app.tests.views.gym_item_common import GymViewCommonCase
import pytz


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

    def test_shows_gyms(self):
        """
        Test that when visited no gyms
        """
        gym_item = GymItem.objects.get(gym__name='Test Gym')
        gym_item.gym_visit_date = None
        gym_item.save()
        self.client.login(username='test', password='password')
        resp = self.client.get(reverse_lazy('gym_list'))
        self.assertTrue('Gyms' in str(resp.content))

    def test_completed_gym_with_raid(self):
        """
        Test that when a raid is active on gym it shows it
        """
        gym = Gym.objects.get(name='Test Gym')
        raid = RaidItem.objects.create(
            gym=gym,
            pokemon='Test Pokemon',
            level=6,
            end_date=(datetime.now(tz=pytz.UTC) + timedelta(hours=1))
        )
        raid.save()
        self.client.login(username='test', password='password')
        resp = self.client.get(reverse_lazy('raid_list'))
        self.assertTrue('Test Pokemon (6)' in str(resp.content))
