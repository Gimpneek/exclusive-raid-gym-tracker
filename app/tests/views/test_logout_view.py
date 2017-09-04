""" Test the logout view """
from django.test import TestCase
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy


class TestLogoutView(TestCase):
    """ Log out view tests """

    def setUp(self):
        """ Set up User for testing """
        super(TestLogoutView, self).setUp()
        self.user = User.objects.create(username='test')
        self.user.set_password('password')
        self.user.save()
        self.client.login(username='test', password='password')
        self.page = self.client.get(reverse_lazy('logout'))

    def test_logs_out_logged_in_user(self):
        """
        Test that visiting the logout page as a logged in user logs them out
        """
        self.assertIsNone(self.client.session.session_key)

    def test_redirects_to_homepage(self):
        """
        Test that logging out redirects to homepage
        """
        self.assertEqual(self.page.url, reverse_lazy('index'))
