""" Test the API for Gyms """

from app.tests.api.personalised.gym_visit_resource.gym_visit_common import \
    GymVisitAPICommonCase


class TestGymVisitResourceModelData(GymVisitAPICommonCase):
    """ Test the API methods for the Gym """

    def test_visit_date(self):
        """
        Test that the visit date for the gym item is returned
        """
        resp = self.api.get(self.url)
        results = resp.data
        self.assertEqual(
            results.get('gym_visit_date'),
            self.visit_date.strftime('%Y-%m-%dT%H:%M:%SZ')
        )

    def test_gym_name(self):
        """
        Test that gym name is returned
        """
        resp = self.api.get(self.url)
        result = resp.data
        self.assertEqual(result.get('gym').get('name'), self.gym.name)
