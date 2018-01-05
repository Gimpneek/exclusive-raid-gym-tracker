from django.contrib.auth.models import User
from app.models.profile import Profile
from app.tests.api.api_common import APICommonCase


class ProfileCollectionCommonCase(APICommonCase):
    """
    Set up the tests for the Profile Collection endpoint
    """

    def setUp(self):
        """
        Set up the tests
        """
        super(ProfileCollectionCommonCase, self).setUp()
        User.objects.create(username='test2')
        self.user2 = User.objects.get(username='test2')
        self.user2.set_password('password')
        self.user2.save()
        self.profile2 = Profile.objects.create(
            user=self.user2
        )
        self.url = '/api/v1/profiles/'
