""" Test the API for Raids """
from datetime import datetime, timedelta
from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from app.models.gym import Gym
from app.models.profile import Profile
from app.models.raid_item import RaidItem
import pytz


class TestRaidApi(TestCase):
    """ Test the API methods for the Raids """

    def setUp(self):
        """ Set up the tests """
        super(TestRaidApi, self).setUp()
        self.gym = Gym.objects.create(
            name='Test Gym',
            location='666,1337',
            image_url='image.jpg'
        )
        self.raid_time = datetime.now(tz=pytz.UTC) + timedelta(hours=1)
        RaidItem.objects.create(
            gym=self.gym,
            pokemon='Test Pokemon',
            level=5,
            end_date=self.raid_time
        )
        User.objects.create(username='test')
        self.user = User.objects.get(username='test')
        self.user.set_password('password')
        self.user.save()
        self.profile = Profile.objects.create(user=self.user)
        self.api = APIClient()
        self.api.login(username='test', password='password')

    def test_gym_list(self):
        """
        Test that a list of Gyms is returned
        """
        RaidItem.objects.create(
            gym=self.gym,
            pokemon='Old Pokemon',
            level=5,
            end_date='1988-01-12 06:00:00+00:00'
        )
        resp = self.api.get('/api/v1/raids/')
        results = resp.data.get('results')
        self.assertEqual(len(results), 2)

    def test_pokemon(self):
        """
        Test that the pokemon for the raid is returned
        """
        resp = self.api.get('/api/v1/raids/')
        results = resp.data.get('results')[0]
        self.assertEqual(results.get('pokemon'), 'Test Pokemon')

    def test_level(self):
        """
        Test that the level for the raid is returned
        """
        resp = self.api.get('/api/v1/raids/')
        results = resp.data.get('results')[0]
        self.assertEqual(results.get('level'), 5)

    def test_end_date(self):
        """
        Test that the end date for the raid is returned
        """
        resp = self.api.get('/api/v1/raids/')
        results = resp.data.get('results')[0]
        self.assertTrue(
            self.raid_time.strftime('%Y-%m-%dT%H:%M') in results['end_date']
        )

    def test_gym_name(self):
        """
        Test that gym name is returned
        """
        resp = self.api.get('/api/v1/raids/')
        result = resp.data.get('results')[0]
        self.assertEqual(result.get('gym').get('name'), self.gym.name)

    def test_gym_image(self):
        """
        Test that gym image is returned
        """
        resp = self.api.get('/api/v1/raids/')
        result = resp.data.get('results')[0]
        self.assertEqual(
            result.get('gym').get('image_url'), self.gym.image_url)

    def test_gym_location(self):
        """
        Test that the location of the gym is returned
        """
        resp = self.api.get('/api/v1/raids/')
        result = resp.data.get('results')[0]
        self.assertEqual(result.get('gym').get('location'), self.gym.location)

    def test_gym_id(self):
        """
        Test that the id of the gym is returned
        """
        resp = self.api.get('/api/v1/raids/')
        result = resp.data.get('results')[0]
        self.assertEqual(result.get('gym').get('id'), self.gym.id)

    def test_not_logged_in(self):
        """
        Test that when user isn't authenticated that the API returns a 404
        """
        self.api.logout()
        resp = self.api.get('/api/v1/raids/')
        self.assertEqual(resp.status_code, 200)

    def test_get_allowed(self):
        """
        Test that get requests are allowed
        """
        resp = self.api.get('/api/v1/raids/')
        self.assertEqual(resp.status_code, 200)

    def test_post_blocked(self):
        """
        Test that post requests are not allowed
        """
        resp = self.api.post(
            '/api/v1/raids/',
            {
                'pokemon': 'Post',
                'end_date': '1990-04-13 06:00:00+00:00',
                'level': 1,
                'gym': 1
            },
            format='json')
        self.assertEqual(resp.status_code, 405)
