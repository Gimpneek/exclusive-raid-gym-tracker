""" Page Object Model for listing """
from .selectors.listing import GYMS_TO_VISIT_CARDS, CARD_CONTENT_TITLE, \
    COMPLETED_GYMS_CARDS, CARD_CONTENT_VISIT_DATE, TITLES, \
    get_link_selector, PROGRESS_BAR, PROGRESS_PERCENTAGE
from .common import BasePage
from datetime import datetime
from selenium.common.exceptions import NoSuchElementException


class ListingPage(BasePage):
    """ Listing Page Object Model """

    def get_yet_to_complete_cards(self):
        """
        Get a list of cards from the yet to complete list
        :return: list of cards from the yet to complete list
        """
        try:
            cards = self.driver.find_elements(*GYMS_TO_VISIT_CARDS)
        except NoSuchElementException:
            cards = []
        return cards

    def get_completed_cards(self):
        """
        Get a list of cards from the completed raids list
        :return: list of cards from the completed raids list
        """
        try:
            cards = self.driver.find_elements(*COMPLETED_GYMS_CARDS)
        except NoSuchElementException:
            cards = []
        return cards

    def get_list_titles(self):
        """
        Get the list of titles
        :return: list of titles
        """
        return self.driver.find_elements(*TITLES)

    @staticmethod
    def get_titles_for_cards(cards):
        """
        Get titles for the supplied list of cards
        :param cards: list of card webelements
        :return: list of titles from the cards
        """
        titles = []
        for card in cards:
            title = card.find_element(*CARD_CONTENT_TITLE)
            titles.append(title.text)
        return titles

    @staticmethod
    def get_visit_dates_for_cards(cards):
        """
        Get visit dates for the supplied list of cards
        :param cards: list of card webelements
        :return: list of datetimes from the cards
        """
        dates = []
        for card in cards:
            date = card.find_element(*CARD_CONTENT_VISIT_DATE)
            date_str = date.text.replace('You last visited this gym on ', '')
            converted_date = datetime.strptime(date_str, '%d/%m/%Y')
            dates.append(converted_date)
        return dates

    @staticmethod
    def get_card_button_by_name(card, button_name):
        """
        Get the button element in the card with supplied text
        :param card: Webelement for gym list card
        :param button_name: Text on the button
        :return: webelement for Gym Item
        """
        return card.find_element(*get_link_selector(button_name))

    def get_progress_bar(self):
        """
        Get the values from progress bar
        :return: progress bar values
        :rtype: dict
        """
        progress_bar = self.driver.find_element(*PROGRESS_BAR)
        return {
            'value': int(progress_bar.get_attribute('value')),
            'max': int(progress_bar.get_attribute('max')),
            'percentage': progress_bar.text
        }

    def get_progress_percentage(self):
        """
        Get the values from percentage under the progress bar
        :return: progress percentage
        :rtype: int
        """
        progress_bar = self.driver.find_element(*PROGRESS_PERCENTAGE)
        return int(progress_bar.text.replace('% complete!', ''))
