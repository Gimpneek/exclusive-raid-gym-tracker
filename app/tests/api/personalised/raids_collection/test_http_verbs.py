""" Test the API for Raids """
from app.tests.api.personalised.raids_collection.raids_collection_common \
    import RaidsCollectionCommonCase


class TestRaidApi(RaidsCollectionCommonCase):
    """ Test the API methods for the Raids """

    def test_not_logged_in(self):
        """
        Test that when user isn't authenticated that the API returns a 401
        """
        self.api.logout()
        resp = self.api.get(self.url)
        self.assertEqual(resp.status_code, 401)

    def test_get_allowed(self):
        """
        Test that get requests are allowed
        """
        resp = self.api.get(self.url)
        self.assertEqual(resp.status_code, 200)

    def test_post_blocked(self):
        """
        Test that post requests are not allowed
        """
        resp = self.api.post(
            self.url,
            {
                'pokemon': 'Post',
                'end_date': '1990-04-13 06:00:00+00:00',
                'level': 1,
                'gym': 1
            },
            format='json')
        self.assertEqual(resp.status_code, 405)

    def test_delete_blocked(self):
        """
        Test that the DELETE verb is not allowed
        """
        resp = self.api.delete(self.url)
        self.assertEqual(resp.status_code, 405)

    def test_put_blocked(self):
        """
        Test that the PUT verb is not allowed
        """
        resp = self.api.put(
            self.url,
            {
                'name': 'PUT',
                'location': 'test',
                'image_url': 'test.jpg'
            },
            format='json'
        )
        self.assertEqual(resp.status_code, 405)
