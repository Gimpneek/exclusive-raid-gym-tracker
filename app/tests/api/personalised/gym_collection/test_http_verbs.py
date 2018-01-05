""" Test the API for Gyms """
from app.tests.api.personalised.gym_collection.gym_common import \
    GymAPICommonCase


class TestGymCollectionHTTPVerbs(GymAPICommonCase):
    """ Test the API methods for the Gym """

    def test_not_logged_in(self):
        """
        Test that when user isn't authenticated that the API returns a 404
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

    def test_post_allowed(self):
        """
        Test that post requests are allowed so it can be used to track gyms
        """
        self.profile.tracked_gyms.remove(self.gym)
        resp = self.api.post(
            self.url,
            {
                'gym_id': self.gym.id
            },
            format='json')
        self.assertEqual(resp.status_code, 201)
        self.assertIn(self.gym, self.profile.tracked_gyms.all())

    def test_post_bad_data(self):
        """
        Test that when a bad POST request it returns a 400
        """
        self.profile.tracked_gyms.remove(self.gym)
        resp = self.api.post(
            self.url,
            {
                'bad_id': self.gym.id
            },
            format='json')
        self.assertEqual(resp.status_code, 400)
        self.assertNotIn(self.gym, self.profile.tracked_gyms.all())

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
