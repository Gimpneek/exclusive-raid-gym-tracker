""" Test the sign up view """
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from app.models.gym import Gym
from app.models.profile import Profile


class TestSignUpView(TestCase):
    """ Sign up view tests """

    def setUp(self):
        """ Set up User for testing """
        super(TestSignUpView, self).setUp()
        Gym.objects.create(
            name='Test Gym',
            location='Test Location'
        )
        self.user = User.objects.create(username='test')
        self.user.set_password('password')
        self.user.save()

    def test_redirects_logged_in_user(self):
        """ Test that a logged in user is redirected to the Gym List """
        self.client.login(username='test', password='password')
        resp = self.client.get(reverse_lazy('signup'))
        self.assertEqual(resp.url, reverse_lazy('gym_list'))

    def test_shows_signup_form(self):
        """
        Test that non-signed in user sees sign up form
        """
        resp = self.client.get(reverse_lazy('signup'))
        self.assertEqual(resp.templates[0].name, 'app/signup.html')

    def test_sign_up_valid(self):
        """
        Test that signing up with a new user creates a profile and
        redirects to Gym List
        """
        profiles = Profile.objects.count()
        resp = self.client.post(
            reverse_lazy('signup'),
            {
                'username': 'new_user',
                'password': 'password'
            }
        )
        self.assertEqual(resp.url, reverse_lazy('gym_list'))
        self.assertGreater(Profile.objects.count(), profiles)

    def test_sign_up_existing_username(self):
        """
        Test that trying to sign up with an existing user shows error on form
        """
        resp = self.client.post(
            reverse_lazy('signup'),
            {
                'username': 'test',
                'password': 'password'
            }, follow=True
        )
        self.assertTrue('username already exists' in str(resp.content))

    def test_sign_up_no_username(self):
        """
        Test that trying to sign up without a username shows an error on form
        """
        resp = self.client.post(
            reverse_lazy('signup'),
            {
                'password': 'password'
            }, follow=True
        )
        self.assertTrue('This field is required' in str(resp.content))

    def test_sign_up_no_password(self):
        """
        Test that trying to sign up without a password shows an error on form
        """
        resp = self.client.post(
            reverse_lazy('signup'),
            {
                'username': 'test',
            }, follow=True
        )
        self.assertTrue('This field is required' in str(resp.content))
