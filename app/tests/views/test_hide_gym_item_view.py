""" Test the hide gym item view """
from django.core.urlresolvers import reverse_lazy
from app.models.gym_item import GymItem
from app.tests.common import create_gym_item
from app.tests.views.gym_item_common import GymViewCommonCase


class TestHideGymItemView(GymViewCommonCase):
    """ Hide Gym Item view tests """

    def setUp(self):
        """ Set up test """
        super(TestHideGymItemView, self).setUp()
        create_gym_item('other', 'Test Gym 1', 'Test Location', '1988-01-12')
        self.other_gym_item = GymItem.objects.get(gym__name='Test Gym 1')

    def test_redirects_logged_out_user(self):
        """ Test that a logged out user is redirected to the Homepage """
        resp = self.client.get(
            reverse_lazy(
                'hide_gym_item',
                kwargs={
                    'gym_item_id': self.gym_item.id
                }
            )
        )
        self.assertTrue(str(reverse_lazy('login')) in resp.url)

    def test_redirects_not_users_item(self):
        """
        Test that redirects to Gym List if Gym Item doesn't belong to the user
        """
        self.client.login(username='test', password='password')
        resp = self.client.get(
            reverse_lazy(
                'hide_gym_item',
                kwargs={
                    'gym_item_id': self.other_gym_item.id
                }
            )
        )
        self.assertEqual(resp.url, reverse_lazy('gym_list'))
        gym_item = GymItem.objects.get(gym__name='Test Gym 1')
        self.assertFalse(gym_item.hidden)

    def test_hides_gym_item_(self):
        """
        Test that sign in user will hide the Gym Item and be shown gym list
        """
        self.client.login(username='test', password='password')
        resp = self.client.get(
            reverse_lazy(
                'hide_gym_item',
                kwargs={
                    'gym_item_id': self.gym_item.id
                }
            )
        )
        self.assertEqual(resp.url, reverse_lazy('gym_list'))
        gym_item = GymItem.objects.get(gym__name='Test Gym')
        self.assertTrue(gym_item.hidden)
