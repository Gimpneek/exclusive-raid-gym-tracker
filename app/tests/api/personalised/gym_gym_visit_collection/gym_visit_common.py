from datetime import datetime
from app.tests.api.api_common import APICommonCase
import pytz


class GymVisitAPICommonCase(APICommonCase):
    """
    Common setup for testing the Gym API endpoints
    """

    def setUp(self):
        """ Set up the tests """
        super(GymVisitAPICommonCase, self).setUp()
        self.visit_date = datetime(1988, 1, 12, 6, 0, 0, tzinfo=pytz.UTC)
        self.profile.tracked_gyms.add(self.gym)
        self.create_gym_visit()
        self.url = '/api/v1/me/gyms/{}/visits/'.format(self.gym.id)


