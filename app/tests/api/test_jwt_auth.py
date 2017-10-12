""" Tests for JSON Web Token endpoint """
from django.test import TestCase
from django.contrib.auth.models import User


class TestJwtAuth(TestCase):
    """
    Test that the django rest framework JWT auth works
    """

    def setUp(self):
        """
        Set up tests
        """
        super(TestJwtAuth, self).setUp()
        User.objects.create(username='test')
        self.user = User.objects.get(username='test')
        self.user.set_password('password')
        self.user.save()

    def test_unauthed(self):
        """
        Test that with no authorisation we get a 401 back
        """
        resp = self.client.get('/api/v1/gyms/')
        self.assertEqual(resp.status_code, 401)

    def test_get_token(self):
        """
        Test that hitting up token endpoint returns token
        """
        resp = self.client.post(
            '/api/v1/api-token-auth/',
            {
                'username': 'test',
                'password': 'password'
            },
            follow=True
        )
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('token' in resp.json().keys())

    def test_authed_access(self):
        """
        Test that hitting up token endpoint returns token
        """
        resp = self.client.post(
            '/api/v1/api-token-auth/',
            {
                'username': 'test',
                'password': 'password'
            }
        )
        token = resp.json().get('token')
        self.assertEqual(resp.status_code, 200)
        authed_resp = self.client.get(
            '/api/v1/gyms/',
            HTTP_AUTHORIZATION='JWT {}'.format(token)
        )
        self.assertEqual(authed_resp.status_code, 200)
