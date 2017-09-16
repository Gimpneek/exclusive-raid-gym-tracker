""" Test the profile view """
from django.test import TestCase
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from app.models.profile import Profile


USERNAME = 'test'
PASSWORD = 'password'


class TestProfileView(TestCase):
    """ Profile view tests """

    def setUp(self):
        """ Set up tests """
        super(TestProfileView, self).setUp()
        user = User.objects.create(username=USERNAME)
        Profile.objects.create(
            user=user,
            pokemon_go_username=USERNAME
        )
        user.set_password('password')
        user.save()

    def test_redirects_logged_out_user(self):
        """ Test that a logged out user is redirected to the Homepage """
        resp = self.client.get(reverse_lazy('profile'))
        self.assertTrue(str(reverse_lazy('login')) in resp.url)

    def test_shows_profile_template(self):
        """
        Test that signed in user sees their username
        """
        self.client.login(username=USERNAME, password=PASSWORD)
        resp = self.client.get(reverse_lazy('profile'))
        self.assertEqual(resp.templates[0].name, 'app/profile.html')
