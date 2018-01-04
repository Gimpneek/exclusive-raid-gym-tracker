""" Test the API for Gyms """
from app.tests.api.personalised.gym_resource.gym_resource_common import \
    GymResourceCommonCase


class TestGymResourceHttpVerbs(GymResourceCommonCase):
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

    def test_post_blocked(self):
        """
        Test that post requests are not allowed
        """
        resp = self.api.post(
            self.url,
            {
                'name': 'Post',
                'location': 'test',
                'image_url': 'test.jpg'
            },
            format='json')
        self.assertEqual(resp.status_code, 405)

    def test_delete_allowed(self):
        """
        Test that the DELETE verb is allowed so it can be used to stop tracking
        Gyms
        """
        self.profile.tracked_gyms.add(self.gym)
        resp = self.api.delete(self.url)
        self.assertEqual(resp.status_code, 301)
        self.assertNotIn(self.gym, self.profile.tracked_gyms.all())

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
