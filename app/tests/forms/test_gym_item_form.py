""" Test the form definition for a Gym Item instance """
from django.test import TestCase
from app.forms.gym_item import GymItemForm
from app.tests.common import create_gym_item


class TestGymItemForm(TestCase):
    """ Test Gym Item Form """

    def setUp(self):
        """ Set up test with Gym Item """
        super(TestGymItemForm, self).setUp()
        self.gym_item = create_gym_item(
            'test', 'Test Gym', 'somewhere', '1988-01-12 12:00:00+01:00')

    def test_last_visit_date_none(self):
        """ Test updating the last visit date to None """
        gym_item_form = GymItemForm(
            instance=self.gym_item,
            data={
                'gym_visit_date': None
            }
        )
        self.assertFalse(gym_item_form.is_valid())

    def test_last_visit_date_updated(self):
        """ Test updating the last visit date """
        gym_item_form = GymItemForm(
            instance=self.gym_item,
            data={
                'gym_visit_date': '1990-04-13T12:00'
            }
        )
        self.assertTrue(gym_item_form.is_valid())
        gym_item_form.save()
        self.assertEqual(
            self.gym_item.gym_visit_date.strftime('%Y-%m-%d %H:%M:%S'),
            '1990-04-13 12:00:00'
        )

    def test_last_visit_date_error(self):
        """ Test updating the last visit date with incorrect values """
        gym_item_form = GymItemForm(
            instance=self.gym_item,
            data={
                'gym_visit_date': 'badness'
            }
        )
        self.assertFalse(gym_item_form.is_valid())
        with self.assertRaises(ValueError):
            gym_item_form.save()
