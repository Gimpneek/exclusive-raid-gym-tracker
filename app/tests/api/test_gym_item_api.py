""" Test the API for Gyms """
from datetime import datetime, timedelta
from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from app.models.gym import Gym
from app.models.gym_item import GymItem
from app.models.profile import Profile
import pytz


class TestGymItemApi(TestCase):
    """ Test the API methods for the Gym """

    def setUp(self):
        """ Set up the tests """
        super(TestGymItemApi, self).setUp()
        self.gym = Gym.objects.create(
            name='Test Gym',
            location='666,1337',
            image_url='image.jpg'
        )
        User.objects.create(username='test')
        self.user = User.objects.get(username='test')
        self.user.set_password('password')
        self.user.save()
        self.profile = Profile.objects.create(user=self.user)
        self.visit_date = datetime(1988, 1, 12, 6, 0, 0, tzinfo=pytz.UTC)
        self.gym_visit = GymItem.objects.create(
            gym=self.gym,
            profile=self.profile,
            gym_visit_date=self.visit_date
        )
        self.api = APIClient()
        self.api.login(username='test', password='password')

    def test_gym_visit_list(self):
        """
        Test that a list of Gym Visits is returned
        """
        GymItem.objects.create(
            gym=self.gym,
            profile=self.profile,
            gym_visit_date=self.visit_date
        )
        resp = self.api.get('/api/v1/gym-visits/')
        results = resp.data.get('results')
        self.assertEqual(len(results), 2)

    def test_visit_date(self):
        """
        Test that the visit date for the gym item is returned
        """
        resp = self.api.get('/api/v1/gym-visits/')
        results = resp.data.get('results')[0]
        self.assertEqual(
            results.get('gym_visit_date'),
            self.visit_date.strftime('%Y-%m-%dT%H:%M:%SZ')
        )

    def test_gym_name(self):
        """
        Test that gym name is returned
        """
        resp = self.api.get('/api/v1/gym-visits/')
        result = resp.data.get('results')[0]
        self.assertEqual(result.get('gym').get('name'), self.gym.name)

    def test_not_logged_in(self):
        """
        Test that when user isn't authenticated that the API returns a 404
        """
        self.api.logout()
        resp = self.api.get('/api/v1/gym-visits/')
        self.assertEqual(resp.status_code, 403)

    def test_get_allowed(self):
        """
        Test that get requests are allowed
        """
        resp = self.api.get('/api/v1/gym-visits/')
        self.assertEqual(resp.status_code, 200)

    def test_post_allowed(self):
        """
        Test that post requests are not allowed
        """
        visit_count = GymItem.objects.all().count()
        resp = self.api.post(
            '/api/v1/gym-visits/',
            {
                'gym': 1,
                'gym_visit_date': '1990-04-13T06:00'
            },
            format='json')
        self.assertEqual(resp.status_code, 201)
        self.assertGreater(GymItem.objects.all().count(), visit_count)

    def test_post_bad_data(self):
        """
        Test that when posting bad data that returns 400
        """
        resp = self.api.post(
            '/api/v1/gym-visits/',
            {
                'gym': 1,
                'gym_visit_date': 'Colin\'s Birthday'
            },
            format='json')
        self.assertEqual(resp.status_code, 400)

    def test_delete_allowed(self):
        """
        Test that can delete a gym visit
        """
        resp = self.api.delete(
            '/api/v1/gym-visits/{}'.format(self.gym_visit.id))
        self.assertEqual(resp.status_code, 301)
        resp = self.api.get('api/v1/gym-visits/{}'.format(self.gym_visit.id))
        self.assertEqual(resp.status_code, 404)
