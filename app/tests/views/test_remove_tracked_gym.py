""" Test the /gym-management/remove/ view """
from django.urls import reverse_lazy
from app.models.profile import Profile
from app.tests.views.gym_item_common import GymViewCommonCase


class TestRemoveTrackedGym(GymViewCommonCase):
    """ Remove Tracked Gym view tests """

    def test_redirects_logged_out_user(self):
        """ Test that a logged out user is redirected to the Homepage """
        resp = self.client.get(
            reverse_lazy(
                'remove_tracked_gym',
                kwargs={
                    'gym_id': self.gym_item.gym.id
                }
            )
        )
        self.assertTrue(str(reverse_lazy('login')) in resp.url)

    def test_removes_tracked_gym(self):
        """
        Test that if the supplied gym is being tracked that it removes that
        gym from the list of tracked gyms
        """
        profile = Profile.objects.get(user=self.user)
        self.client.login(username='test', password='password')
        resp = self.client.get(
            reverse_lazy(
                'remove_tracked_gym',
                kwargs={
                    'gym_id': self.gym_item.gym.id
                }
            )
        )
        self.assertTrue(str(reverse_lazy('gym_management')) in resp.url)
        self.assertTrue(self.gym_item.gym not in profile.tracked_gyms.all())
        self.assertEqual(profile.tracked_gyms.count(), 0)

    def test_removing_untracked_gym(self):
        """
        Test that when if there's no tracked gyms that it raises an exception
        """
        profile = Profile.objects.get(user=self.user)
        profile.tracked_gyms.remove(self.gym_item.gym)
        self.client.login(username='test', password='password')
        resp = self.client.get(
            reverse_lazy(
                'remove_tracked_gym',
                kwargs={
                    'gym_id': self.gym_item.gym.id
                }
            )
        )
        self.assertEqual(resp.status_code, 400)
