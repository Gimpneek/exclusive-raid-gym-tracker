""" Test the homepage view """
from django.test import TestCase
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy


class TestHomepageView(TestCase):
    """ Homepage view tests """

    def setUp(self):
        """ Set up User for testing """
        super(TestHomepageView, self).setUp()
        self.user = User.objects.create(username='test')
        self.user.set_password('password')
        self.user.save()

    def test_redirects_logged_in_user(self):
        """ Test that a logged in user is redirected to the Gym List """
        self.client.login(username='test', password='password')
        resp = self.client.get(reverse_lazy('index'))
        self.assertEqual(resp.url, reverse_lazy('gym_list'))

    def test_shows_login_form(self):
        """
        Test that non-signed in user sees login form
        """
        resp = self.client.get(reverse_lazy('index'))
        self.assertEqual(resp.templates[0].name, 'app/homepage.html')
