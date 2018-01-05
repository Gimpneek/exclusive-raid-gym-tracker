from app.tests.api.api_common import APICommonCase


class GymAPICommonCase(APICommonCase):
    """
    Common setup for testing the Gym API endpoints
    """

    def setUp(self):
        """ Set up the tests """
        super(GymAPICommonCase, self).setUp()
        self.url = '/api/v1/gyms/'
