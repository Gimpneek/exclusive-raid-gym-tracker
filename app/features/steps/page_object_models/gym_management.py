""" Page Object Model - Gym Management Page """
from selenium.webdriver.common.by import By
from .selectors.gym_management import TRACKED_GYMS_TABLE_ROW, REMOVE_BUTTON, \
    TABLE_COLUMNS
from .selectors.listing import SEARCH_BAR
from .common import BasePage
from .listing import ListingPage


class GymManagementPage(BasePage):
    """
    Page Object Model for Gym Management Page
    """

    def find_tracked_gym(self, gym_name):
        """
        Locate the gym in the tracked gyms list

        :return: WebElement of row with Gym in it or None
        """
        gyms = self.driver.find_elements(*TRACKED_GYMS_TABLE_ROW)
        for gym in gyms:
            if gym_name in gym.text:
                return gym
        return None

    def remove_tracked_gym(self, gym_row):
        """
        Press the Remove button the supplied table row containing the Gym
        to stop tracking

        :param gym_row: WebElement of the table row that the Gym is in
        """
        columns = gym_row.find_elements(*TABLE_COLUMNS)
        remove_button = columns[1].find_element(*REMOVE_BUTTON)
        button_selector = (
            By.CSS_SELECTOR,
            'a[href="{}"]'.format(remove_button.get_attribute('href'))
        )
        self.click_and_verify_change(
            remove_button,
            button_selector,
            hidden=True
        )

    def enter_search_term(self, term):
        """
        Enter a search term into the search bar

        :param term: Term to enter
        """
        page = ListingPage(self.driver)
        page.enter_search_term(term)

    def press_suggested_gym(self, gym):
        """
        Press the suggested gym in the dropdown

        :param gym: Gym to find
        """
        page = ListingPage(self.driver)
        suggestions = page.get_search_suggestions()
        option = None
        for suggestion in suggestions:
            if suggestion.text == gym:
                option = suggestion
        assert option
        page.click_and_verify_change(option, SEARCH_BAR)
