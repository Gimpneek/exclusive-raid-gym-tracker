from app.tests.api.api_common import APICommonCase


class ProfileCommonCase(APICommonCase):
    """
    Set up the tests for the Profile endpoint
    """

    def setUp(self):
        """
        Set up the tests
        """
        super(ProfileCommonCase, self).setUp()
        self.url = '/api/v1/me/'
