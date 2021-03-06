""" Test the gym item view """
from datetime import datetime
from django.urls import reverse_lazy
from app.models.gym import Gym
from app.models.gym_item import GymItem
from app.models.raid_item import RaidItem
from app.models.profile import Profile
from app.tests.views.gym_item_common import GymViewCommonCase
import pytz


class TestAddRaidView(GymViewCommonCase):
    """ Gym Item view tests """

    def test_redirects_logged_out_user(self):
        """ Test that a logged out user is redirected to the Homepage """
        resp = self.client.get(
            reverse_lazy(
                'add_gym_raid',
                kwargs={
                    'gym_id': self.gym_item.id
                }
            )
        )
        self.assertTrue(str(reverse_lazy('login')) in resp.url)

    def test_shows_gym_item(self):
        """
        Test that signed in user sees Gym Item
        """
        self.client.login(username='test', password='password')
        resp = self.client.get(
            reverse_lazy(
                'add_gym_raid',
                kwargs={
                    'gym_id': self.gym_item.id
                }
            )
        )
        self.assertEqual(resp.templates[0].name, 'app/add_gym_raid.html')

    def test_submit_invalid_date(self):
        """
        Test that shows error on form when submitting a bad date
        """
        self.client.login(username='test', password='password')
        resp = self.client.post(
            reverse_lazy(
                'add_gym_raid',
                kwargs={
                    'gym_id': self.gym_item.id
                }
            ),
            data={
                'gym_visit_date': 'bad_string'
            }
        )
        self.assertTrue('Invalid date entered' in str(resp.content))

    def test_changes_submitted_date(self):
        """
        Test that on submitting a valid date it updates the gym_item
        """
        self.client.login(username='test', password='password')
        resp = self.client.post(
            reverse_lazy(
                'add_gym_raid',
                kwargs={
                    'gym_id': self.gym_item.id
                }
            ),
            data={
                'gym_visit_date': '1990-04-13T12:00'
            }
        )
        self.assertEqual(resp.url, reverse_lazy('gym_list'))
        gym_item = GymItem.objects.filter(gym__name='Test Gym').last()
        self.assertEqual(
            gym_item.gym_visit_date.strftime('%Y-%m-%d %H:%M:%S'),
            '1990-04-13 12:01:00'
        )

    def test_starts_tracking_gym(self):
        """
        Test that if gym adding raid to isn't currently in the user's gym list
        that the gym is added to that list
        """
        new_gym = Gym.objects.create(name='Untracked Gym', location='te,st')
        self.client.login(username='test', password='password')
        resp = self.client.post(
            reverse_lazy(
                'add_gym_raid',
                kwargs={
                    'gym_id': new_gym.id
                }
            ),
            data={
                'gym_visit_date': '1990-04-13T12:00'
            }
        )
        self.assertEqual(resp.url, reverse_lazy('gym_list'))
        profile = Profile.objects.get(user=self.user)
        self.assertTrue(new_gym in profile.tracked_gyms.all())

    def test_no_date_set(self):
        """
        Test that when no date is set on gym item it shows an empty input
        """
        self.gym_item.last_visit_date = None
        self.gym_item.save()
        self.client.login(username='test', password='password')
        resp = self.client.get(
            reverse_lazy(
                'add_gym_raid',
                kwargs={
                    'gym_id': self.gym_item.id
                }
            )
        )
        input_str = 'name="gym_visit_date" type="datetime-local" value="{}"'
        input_el = input_str.format(
            datetime.now(tz=pytz.timezone('Europe/London'))
            .strftime('%Y-%m-%dT%H:%M')
        )
        self.assertTrue(input_el in str(resp.content))

    def test_recent_raids(self):
        """
        Test that the recent raids table is shown if raids have happened at
        the gym
        """
        RaidItem.objects.create(
            pokemon='Colin',
            level=6,
            end_date='1988-01-12 06:00:00+00:00',
            gym=self.gym_item.gym
        )
        self.client.login(username='test', password='password')
        resp = self.client.get(
            reverse_lazy(
                'add_gym_raid',
                kwargs={
                    'gym_id': self.gym_item.id
                }
            )
        )
        self.assertTrue('Recent Raids on this Gym' in str(resp.content))

    def test_no_recent_raids(self):
        """
        Test that the recent raids table is not shown if no raids have happened
        at the gym
        """
        self.client.login(username='test', password='password')
        resp = self.client.get(
            reverse_lazy(
                'add_gym_raid',
                kwargs={
                    'gym_id': self.gym_item.id
                }
            )
        )
        self.assertTrue('Recent Raids on this Gym' not in str(resp.content))
