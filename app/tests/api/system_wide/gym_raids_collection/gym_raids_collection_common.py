from app.tests.api.api_common import APICommonCase


class GymRaidsCollectionCommonCase(APICommonCase):
    """
    Set up the tests for Gym Raids endpoint
    """

    def setUp(self):
        """ Set up the tests """
        super(GymRaidsCollectionCommonCase, self).setUp()
        self.url = '/api/v1/gyms/{}/raids/'.format(self.gym.id)
