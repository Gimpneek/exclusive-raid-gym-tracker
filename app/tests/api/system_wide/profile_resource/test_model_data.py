""" Test the API for Gyms """
from app.tests.api.personalised.profile_resource.profile_common import \
    ProfileCommonCase


class TestProfileModelData(ProfileCommonCase):
    """ Test the API methods for the Profile """

    def test_profile_name(self):
        """
        Test that profile's username is returned
        """
        resp = self.api.get(self.url)
        result = resp.data
        self.assertEqual(result.get('username'), self.user.username)

    def test_profile_pogo_name(self):
        """
        Test that the Pokemon GO username is returned
        """
        resp = self.api.get(self.url)
        result = resp.data
        self.assertEqual(
            result.get('pokemon_go_username'),
            self.profile.pokemon_go_username
        )
