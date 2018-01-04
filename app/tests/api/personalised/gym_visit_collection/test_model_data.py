""" Test the API for Gyms """

from app.tests.api.personalised.gym_visit_collection.gym_visit_common import \
    GymVisitAPICommonCase


class TestGymVisitCollectionModelData(GymVisitAPICommonCase):
    """ Test the API methods for the Gym """

    def test_gym_visit_list(self):
        """
        Test that a list of Gym Visits is returned
        """
        self.create_gym_visit()
        resp = self.api.get(self.url)
        results = resp.data
        self.assertEqual(len(results), 2)

    def test_visit_date(self):
        """
        Test that the visit date for the gym item is returned
        """
        resp = self.api.get(self.url)
        results = resp.data[0]
        self.assertEqual(
            results.get('gym_visit_date'),
            self.visit_date.strftime('%Y-%m-%dT%H:%M:%SZ')
        )

    def test_gym_name(self):
        """
        Test that gym name is returned
        """
        resp = self.api.get(self.url)
        result = resp.data[0]
        self.assertEqual(result.get('gym').get('name'), self.gym.name)
