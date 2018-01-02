""" Test the API for Gyms """
from datetime import datetime, timedelta
from app.models.gym import Gym
from app.models.gym_item import GymItem
from app.models.raid_item import RaidItem
from app.tests.api.system_wide.gym_collection.gym_common import \
    GymAPICommonCase
import pytz


class TestGymCollectionModelData(GymAPICommonCase):
    """ Test the API methods for the Gym """

    def test_gym_list(self):
        """
        Test that a list of Gyms is returned
        """
        Gym.objects.create(
            name='Test Gym 2',
            location='666,1337',
            image_url='image.jpg'
        )
        resp = self.api.get('/api/v1/gyms/')
        results = resp.data.get('results')
        self.assertEqual(len(results), 2)

    def test_active_raid(self):
        """
        Test that active raid data is returned if a Gym has an active raid on
        it
        """
        raid_time = datetime.now(tz=pytz.UTC) + timedelta(hours=1)
        RaidItem.objects.create(
            gym=self.gym,
            pokemon='Test Pokemon',
            level=5,
            end_date=raid_time
        )
        resp = self.api.get('/api/v1/gyms/')
        results = resp.data.get('results')[0]
        self.assertEqual(results.get('raid').get('pokemon'), 'Test Pokemon')
        self.assertEqual(results.get('raid').get('level'), 5)
        self.assertTrue('0:59:' in results.get('raid').get('time_left'))

    def test_visited_gym(self):
        """
        Test that if a gym has been visited the gym_visit_date is returned
        """
        visit_date = datetime(1988, 1, 12, 6, 0, 0, tzinfo=pytz.UTC)
        GymItem.objects.create(
            gym=self.gym,
            profile=self.profile,
            gym_visit_date=visit_date
        )
        resp = self.api.get('/api/v1/gyms/')
        results = resp.data.get('results')[0]
        self.assertEqual(results.get('gym_visit_date'), visit_date)

    def test_gym_name(self):
        """
        Test that gym name is returned
        """
        resp = self.api.get('/api/v1/gyms/')
        result = resp.data.get('results')[0]
        self.assertEqual(result.get('name'), self.gym.name)

    def test_gym_image(self):
        """
        Test that gym image is returned
        """
        resp = self.api.get('/api/v1/gyms/')
        result = resp.data.get('results')[0]
        self.assertEqual(result.get('image_url'), self.gym.image_url)

    def test_gym_location(self):
        """
        Test that the location of the gym is returned
        """
        resp = self.api.get('/api/v1/gyms/')
        result = resp.data.get('results')[0]
        self.assertEqual(result.get('location'), self.gym.location)

    def test_gym_id(self):
        """
        Test that the location of the gym is returned
        """
        resp = self.api.get('/api/v1/gyms/')
        result = resp.data.get('results')[0]
        self.assertEqual(result.get('id'), self.gym.id)
