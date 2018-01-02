""" Test the API for Gyms """

from app.tests.api.personalised.gym_tracking_resource.gym_tracking_common \
    import GymTrackingAPICommonCase


class TestGymTrackingResourceHttpVerbs(GymTrackingAPICommonCase):
    """ Test the API methods for the Gym """

    def test_not_logged_in(self):
        """
        Test that when user isn't authenticated that the API returns a 404
        """
        self.api.logout()
        resp = self.api.get(self.url)
        self.assertEqual(resp.status_code, 401)

    def test_get_blocked(self):
        """
        Test that get requests are allowed
        """
        resp = self.api.get(self.url)
        self.assertEqual(resp.status_code, 405)

    def test_post_allowed(self):
        """
        Test that post requests are not allowed
        """
        resp = self.api.post(
            self.url,
            {
                'gym': self.gym.id
            },
            format='json')
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(self.profile.tracked_gyms.all()[0], self.gym)

    def test_delete_allowed(self):
        """
        Test that can delete a gym visit
        """
        self.profile.tracked_gyms.add(self.gym)
        resp = self.api.delete(self.url)
        self.assertEqual(resp.status_code, 301)
        self.assertEqual(self.profile.tracked_gyms.all(), [])

    def test_put_blocked(self):
        """
        Test that the PUT verb is not allowed
        """
        resp = self.api.put(
            self.url,
            {
                'gym': 1,
                'gym_visit_date': '1990-04-13T06:00'
            },
            format='json'
        )
        self.assertEqual(resp.status_code, 405)
