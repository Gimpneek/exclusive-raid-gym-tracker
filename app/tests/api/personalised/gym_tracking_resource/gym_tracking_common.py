from datetime import datetime
from app.tests.api.api_common import APICommonCase
import pytz


class GymTrackingAPICommonCase(APICommonCase):
    """
    Common setup for testing the Gym API endpoints
    """

    def setUp(self):
        """ Set up the tests """
        super(GymTrackingAPICommonCase, self).setUp()
        self.url = '/api/v1/me/gyms/{}/track/'.format(self.gym.id)


