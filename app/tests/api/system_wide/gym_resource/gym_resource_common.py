from app.tests.api.api_common import APICommonCase


class GymResourceCommonCase(APICommonCase):
    """
    Set up the tests for the Gym Resource endpoint tests
    """

    def setUp(self):
        """ Set up the tests """
        super(GymResourceCommonCase, self).setUp()
        self.url = '/api/v1/gyms/{}/'.format(self.gym.id)
