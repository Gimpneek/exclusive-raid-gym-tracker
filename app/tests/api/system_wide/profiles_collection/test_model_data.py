""" Test the API for Gyms """
from app.tests.api.system_wide.profiles_collection\
    .profile_collection_common import ProfileCollectionCommonCase


class TestProfileCollectionModelData(ProfileCollectionCommonCase):
    """ Test the API methods for the Profile """

    def test_profile_list(self):
        """
        Test that a list of Gyms is returned
        """
        resp = self.api.get(self.url)
        results = resp.data.get('results')
        self.assertEqual(len(results), 2)

    def test_profile_name(self):
        """
        Test that profile's username is returned
        """
        resp = self.api.get(self.url)
        result = resp.data.get('results')[0]
        self.assertEqual(result.get('username'), self.user.username)

    def test_profile_pogo_name(self):
        """
        Test that the Pokemon GO username is returned
        """
        resp = self.api.get(self.url)
        result = resp.data.get('results')[0]
        self.assertEqual(
            result.get('pokemon_go_username'),
            self.profile.pokemon_go_username
        )
