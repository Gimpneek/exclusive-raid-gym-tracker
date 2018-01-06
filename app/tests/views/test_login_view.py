""" Test the log in view """
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse_lazy


class TestLogInView(TestCase):
    """ Log in view tests """

    def setUp(self):
        """ Set up User for testing """
        super(TestLogInView, self).setUp()
        self.user = User.objects.create(username='test')
        self.user.set_password('password')
        self.user.save()

    def test_redirects_logged_in_user(self):
        """ Test that a logged in user is redirected to the Gym List """
        self.client.login(username='test', password='password')
        resp = self.client.get(reverse_lazy('login'))
        self.assertEqual(resp.url, reverse_lazy('gym_list'))

    def test_shows_login_form(self):
        """
        Test that non-signed in user sees login form
        """
        resp = self.client.get(reverse_lazy('login'))
        self.assertEqual(resp.templates[0].name, 'app/login.html')

    def test_login_valid(self):
        """
        Test that logging in redirects to Gym List
        """
        resp = self.client.post(
            reverse_lazy('login'),
            {
                'username': 'test',
                'password': 'password'
            }
        )
        self.assertEqual(resp.url, reverse_lazy('gym_list'))

    def test_login_no_user_in_system(self):
        """
        Test that trying to log in with a non-existent user
        """
        resp = self.client.post(
            reverse_lazy('login'),
            {
                'username': 'new_user',
                'password': 'password'
            }, follow=True
        )
        self.assertTrue('Unable to login with '
                        'provided credentials' in str(resp.content))

    def test_login_no_username(self):
        """
        Test that trying to login without a username shows an error on form
        """
        resp = self.client.post(
            reverse_lazy('login'),
            {
                'password': 'password'
            }, follow=True
        )
        self.assertTrue('Unable to login with '
                        'provided credentials' in str(resp.content))

    def test_login_no_password(self):
        """
        Test that trying to login without a password shows an error on form
        """
        resp = self.client.post(
            reverse_lazy('login'),
            {
                'username': 'test',
            }, follow=True
        )
        self.assertTrue('Unable to login with '
                        'provided credentials' in str(resp.content))
