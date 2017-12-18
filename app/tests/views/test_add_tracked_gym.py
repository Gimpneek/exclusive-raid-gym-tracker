""" Test the /gym-management/add/ view """
from django.core.urlresolvers import reverse_lazy
from app.models.profile import Profile
from app.tests.views.gym_item_common import GymViewCommonCase


class TestAddTrackedGym(GymViewCommonCase):
    """ Add Tracked Gym view tests """

    def test_redirects_logged_out_user(self):
        """ Test that a logged out user is redirected to the Homepage """
        resp = self.client.get(
            reverse_lazy(
                'add_tracked_gym',
                kwargs={
                    'gym_id': self.gym_item.gym.id
                }
            )
        )
        self.assertTrue(str(reverse_lazy('login')) in resp.url)

    def test_adds_untracked_gym(self):
        """
        Test that if the supplied gym isn't being tracked that it adds that
        gym to the list of tracked gyms
        """
        profile = Profile.objects.get(user=self.user)
        profile.tracked_gyms.remove(self.gym_item.gym)
        self.client.login(username='test', password='password')
        resp = self.client.get(
            reverse_lazy(
                'add_tracked_gym',
                kwargs={
                    'gym_id': self.gym_item.gym.id
                }
            )
        )
        self.assertTrue(str(reverse_lazy('gym_management')) in resp.url)
        self.assertTrue(self.gym_item.gym in profile.tracked_gyms.all())
        self.assertEqual(profile.tracked_gyms.count(), 1)

    def test_keeps_tracked_gym(self):
        """
        Test that when if the supplied gym is being tracked that it's kept and
        a duplicate isn't added
        """
        profile = Profile.objects.get(user=self.user)
        self.client.login(username='test', password='password')
        resp = self.client.get(
            reverse_lazy(
                'add_tracked_gym',
                kwargs={
                    'gym_id': self.gym_item.gym.id
                }
            )
        )
        self.assertTrue(str(reverse_lazy('gym_management')) in resp.url)
        self.assertTrue(self.gym_item.gym in profile.tracked_gyms.all())
        self.assertEqual(profile.tracked_gyms.count(), 1)
