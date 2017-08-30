""" Page Object Model for forms """
from .selectors.forms import USERNAME_INPUT, PASSWORD_INPUT, \
    SUBMIT_BUTTON, ERROR_MESSAGE, LAST_VISIT_DATE_INPUT, \
    CANCEL_BUTTON, REMOVE_RAID_BUTTON
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

    def enter_last_visit_date(self, date):
        """
        Enter supplied last visit date
        :param date: Date string to enter
        """
        form_input = self.driver.find_element(*LAST_VISIT_DATE_INPUT)
        if self.driver.capabilities.get('browserName') == 'phantomjs':
            form_input.clear()
        form_input.send_keys(date)

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

    def cancel_form(self):
        """
        Press the cancel button
        """
        cancel_button = self.driver.find_element(*CANCEL_BUTTON)
        self.click_and_verify_change(cancel_button, CANCEL_BUTTON, hidden=True)

    def remove_raid(self):
        """
        Press the Remove Raid Button
        """
        remove_button = self.driver.find_element(*REMOVE_RAID_BUTTON)
        self.click_and_verify_change(
            remove_button, REMOVE_RAID_BUTTON, hidden=True)
