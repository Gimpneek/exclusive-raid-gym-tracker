""" Test the gym-management view """
from django.urls import reverse_lazy
from app.models.profile import Profile
from app.tests.views.gym_item_common import GymViewCommonCase


class TestGymManagementView(GymViewCommonCase):
    """ Gym Management view tests """

    def test_redirects_logged_out_user(self):
        """ Test that a logged out user is redirected to the Homepage """
        resp = self.client.get(
            reverse_lazy(
                'gym_management'
            )
        )
        self.assertTrue(str(reverse_lazy('login')) in resp.url)

    def test_tracked_gyms(self):
        """
        Test that when there's tracked gyms that the gym list is shown
        """
        self.client.login(username='test', password='password')
        resp = self.client.get(
            reverse_lazy(
                'gym_management'
            )
        )
        self.assertTrue('Gyms' in str(resp.content))

    def test_no_tracked_gyms(self):
        """
        Test that when if there's no tracked gyms that the gym list isn't shown
        """
        profile = Profile.objects.get(user=self.user)
        profile.tracked_gyms.remove(self.gym_item.gym)
        self.client.login(username='test', password='password')
        resp = self.client.get(
            reverse_lazy(
                'gym_management'
            )
        )
        self.assertTrue('Gyms' not in str(resp.content))
