""" Page Object Model - Common Methods """
import selenium.webdriver.support.expected_conditions as ec
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By


class BasePage(object):
    """ Common Methods for Page Object Model """

    def __init__(self, driver):
        """ Initialise class """
        self.driver = driver
        self.default_wait = 20

    def wait_for_element(self, element_selector, hidden=False, wait_time=None):
        """
        Wrapper around WebDriverWait to wait for specified element to become
        visible
        :param element_selector: Element Selector tuple
        :type element_selector: tuple
        :param hidden: Check if element is hidden or not
        :type hidden: bool
        :param wait_time: Custom time to wait
        :type wait_time: int
        """
        condition = ec.visibility_of_element_located(element_selector)
        if hidden:
            condition = ec.invisibility_of_element_located(element_selector)
        if not wait_time:
            wait_time = self.default_wait
        ui.WebDriverWait(self.driver, wait_time).until(condition)

    def click_and_verify_change(self, el_to_click, el_to_verify, hidden=False):
        """
        Wrapper around clicking an element and then waiting for a change in the
        page and verifying said change by ensuring an element is visible
        :param el_to_click: Element to click to induce change
        :type el_to_click: WebdriverElement
        :param el_to_verify: Element to look for to verify change
        :type el_to_verify: WebDriverElement
        :param hidden: Should check for if element is now hidden or not
        :type hidden: bool
        """
        el_to_click.click()
        self.wait_for_element(el_to_verify, hidden=hidden)

    def enter_input_value(self, element, value):
        """
        Enter a value into an input field
        :param element: webelement we want to add value to
        :type element: WebdriverElement
        :param value: Value we want to add
        :type value: str
        """
        element.send_keys(value)
        ui.WebDriverWait(self.driver, self.default_wait).until(
            ec.text_to_be_present_in_element_value(
                self.get_locator(element), value))

    @staticmethod
    def get_locator(element):
        """
        Get locator for element
        :param element: webelement we want to generate locator for
        :type element: WebDriverElement
        :return: Locator for supplied element
        :rtype: tuple
        """
        return By.NAME, element.get_attribute('name')
