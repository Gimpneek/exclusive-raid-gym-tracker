from app.tests.api.api_common import APICommonCase


class RaidsCollectionCommonCase(APICommonCase):
    """
    Set up the Raids Collection tests
    """

    def setUp(self):
        """
        Set up the tests
        """
        super(RaidsCollectionCommonCase, self).setUp()
        self.url = '/api/v1/raids/'
