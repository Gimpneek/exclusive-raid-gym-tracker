""" user form tests """
from django.test import TestCase
from django.contrib.auth.models import User
from app.forms.user import UserForm


class TestUserForm(TestCase):
    """ Test the user form """

    def test_valid(self):
        """
        Test the form is valid when both username and password supplied
        """
        form = UserForm(
            {
                'username': 'test',
                'password': 'password'
            }
        )
        self.assertTrue(form.is_valid())

    def test_invalid_no_username(self):
        """ Test that the form is invalid if no username is supplied """
        form = UserForm(
            {
                'password': 'password'
            }
        )
        self.assertFalse(form.is_valid())

    def test_invalid_no_password(self):
        """ Test that the form is invalid if no password is supplied """
        form = UserForm(
            {
                'username': 'test'
            }
        )
        self.assertFalse(form.is_valid())

    def test_save(self):
        """ Test creates user when valid form is sent """
        users = User.objects.count()
        form = UserForm(
            {
                'username': 'test',
                'password': 'password'
            }
        )
        form.save()
        self.assertGreater(User.objects.count(), users)
