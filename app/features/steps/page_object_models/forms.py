""" Page Object Model for forms """
from .selectors.forms import USERNAME_INPUT, PASSWORD_INPUT, \
    SUBMIT_BUTTON, ERROR_MESSAGE
from .common import BasePage


class FormPage(BasePage):
    """ Form Page Object Model """

    def enter_username(self, username):
        """
        Enter username into the username form input
        :param username: Username to enter
        """
        form_input = self.driver.find_element(*USERNAME_INPUT)
        self.enter_input_value(form_input, username)

    def enter_password(self, password):
        """
        Enter password into the password form input
        :param password: Password to enter
        """
        form_input = self.driver.find_element(*PASSWORD_INPUT)
        self.enter_input_value(form_input, password)

    def submit_form(self, expect_error=False):
        """
        Submit the form
        :param expect_error: If expect error message
        """
        submit_button = self.driver.find_element(*SUBMIT_BUTTON)
        hidden = True
        if expect_error:
            hidden = False
        self.click_and_verify_change(
            submit_button, USERNAME_INPUT, hidden=hidden)

    def get_error_message(self):
        """ Get the error message on the form """
        self.wait_for_element(ERROR_MESSAGE)
        error_element = self.driver.find_element(*ERROR_MESSAGE)
        return error_element.text
