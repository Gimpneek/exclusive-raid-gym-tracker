""" Test the API for Raids """
from app.models.raid_item import RaidItem
from app.tests.api.personalised.raids_collection.raids_collection_common \
    import RaidsCollectionCommonCase


class TestRaidApi(RaidsCollectionCommonCase):
    """ Test the API methods for the Raids """

    def test_gym_list(self):
        """
        Test that a list of Gyms is returned
        """
        RaidItem.objects.create(
            gym=self.gym,
            pokemon='Old Pokemon',
            level=5,
            end_date='1988-01-12 06:00:00+00:00'
        )
        resp = self.api.get(self.url)
        results = resp.data.get('results')
        self.assertEqual(len(results), 2)

    def test_pokemon(self):
        """
        Test that the pokemon for the raid is returned
        """
        resp = self.api.get(self.url)
        results = resp.data.get('results')[0]
        self.assertEqual(results.get('pokemon'), 'Test Pokemon')

    def test_level(self):
        """
        Test that the level for the raid is returned
        """
        resp = self.api.get(self.url)
        results = resp.data.get('results')[0]
        self.assertEqual(results.get('level'), 5)

    def test_end_date(self):
        """
        Test that the end date for the raid is returned
        """
        resp = self.api.get(self.url)
        results = resp.data.get('results')[0]
        self.assertTrue(
            self.raid_time.strftime('%Y-%m-%dT%H:%M') in results['end_date']
        )

    def test_gym_name(self):
        """
        Test that gym name is returned
        """
        resp = self.api.get(self.url)
        result = resp.data.get('results')[0]
        self.assertEqual(result.get('gym').get('name'), self.gym.name)

    def test_gym_image(self):
        """
        Test that gym image is returned
        """
        resp = self.api.get(self.url)
        result = resp.data.get('results')[0]
        self.assertEqual(
            result.get('gym').get('image_url'), self.gym.image_url)

    def test_gym_location(self):
        """
        Test that the location of the gym is returned
        """
        resp = self.api.get(self.url)
        result = resp.data.get('results')[0]
        self.assertEqual(result.get('gym').get('location'), self.gym.location)

    def test_gym_id(self):
        """
        Test that the id of the gym is returned
        """
        resp = self.api.get(self.url)
        result = resp.data.get('results')[0]
        self.assertEqual(result.get('gym').get('id'), self.gym.id)
