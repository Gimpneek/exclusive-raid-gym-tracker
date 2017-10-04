""" Test the API for Gyms """
from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from app.models.profile import Profile


class TestProfileApi(TestCase):
    """ Test the API methods for the Profile """

    def setUp(self):
        """ Set up the tests """
        super(TestProfileApi, self).setUp()
        User.objects.create(username='test')
        self.user = User.objects.get(username='test')
        self.user.set_password('password')
        self.user.save()
        self.profile = Profile.objects.create(
            user=self.user,
            pokemon_go_username='Gimpneek'
        )
        self.api = APIClient()
        self.api.login(username='test', password='password')

    def test_profile_name(self):
        """
        Test that profile's username is returned
        """
        resp = self.api.get('/api/v1/profiles/{}/'.format(self.profile.id))
        result = resp.data
        self.assertEqual(result.get('username'), self.user.username)

    def test_profile_pogo_name(self):
        """
        Test that the Pokemon GO username is returned
        """
        resp = self.api.get('/api/v1/profiles/{}/'.format(self.profile.id))
        result = resp.data
        self.assertEqual(
            result.get('pokemon_go_username'),
            self.profile.pokemon_go_username
        )

    def test_not_logged_in(self):
        """
        Test that when user isn't authenticated that the API returns a 404
        """
        self.api.logout()
        resp = self.api.get('/api/v1/profiles/{}/'.format(self.profile.id))
        self.assertEqual(resp.status_code, 401)

    def test_get_allowed(self):
        """
        Test that get requests are allowed
        """
        resp = self.api.get('/api/v1/profiles/{}/'.format(self.profile.id))
        self.assertEqual(resp.status_code, 200)

    def test_post_blocked(self):
        """
        Test that post requests are not allowed
        """
        resp = self.api.post(
            '/api/v1/profiles/{}/'.format(self.profile.id),
            {},
            format='json')
        self.assertEqual(resp.status_code, 405)
