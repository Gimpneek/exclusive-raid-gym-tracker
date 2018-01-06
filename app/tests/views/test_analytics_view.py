""" Test the analytics view """
from datetime import datetime
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from app.models.profile import Profile
from app.models.gym import Gym
from app.models.raid_item import RaidItem
import pytz


USERNAME = 'test'
PASSWORD = 'password'


class TestAnalyticsView(TestCase):
    """ Profile view tests """

    def setUp(self):
        """ Set up tests """
        super(TestAnalyticsView, self).setUp()
        user = User.objects.create(username=USERNAME)
        Profile.objects.create(
            user=user,
            pokemon_go_username=USERNAME
        )
        user.set_password('password')
        user.save()

    def test_shows_analytics_signed_in(self):
        """
        Test that username sees Analytics
        """
        self.client.login(username=USERNAME, password=PASSWORD)
        resp = self.client.get(reverse_lazy('analytics'))
        self.assertEqual(
            resp.templates[0].name, 'app/analytics_dashboard.html')

    def test_shows_analytics_logged_out(self):
        """
        Test that username sees Analytics
        """
        resp = self.client.get(reverse_lazy('analytics'))
        self.assertEqual(
            resp.templates[0].name, 'app/analytics_dashboard.html')

    def test_top_ten_gyms(self):
        """
        Test that limits top gyms to 10 items
        """
        for i in range(0, 11):
            gym = Gym.objects.create(
                name='Test Gym {}'.format(i),
                location='1337,666'
            )
            RaidItem.objects.create(
                gym=gym,
                pokemon='Test',
                level=5,
                end_date=datetime.now(tz=pytz.UTC)
            )
        resp = self.client.get(reverse_lazy('analytics'))
        self.assertIn('Top 10 Active Gyms', str(resp.content))
