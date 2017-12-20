""" Page Object Model for listing """
from .selectors.listing import GYMS_TO_VISIT_CARDS, CARD_CONTENT_TITLE, \
    COMPLETED_GYMS_CARDS, CARD_CONTENT_VISIT_DATE, TITLES, \
    get_link_selector, PROGRESS_BAR, PROGRESS_PERCENTAGE, SEARCH_BAR, \
    SEARCH_SUGGESTIONS, CARD_HEADER, RAID_BANNER, PARENT_CARD, CARDS
from .common import BasePage
from datetime import datetime
from selenium.common.exceptions import NoSuchElementException
import time


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

    def get_active_raid_cards(self):
        """
        Get a list of cards from the active cards list
        :return: list of cards from the active cards list
        """
        try:
            raid_banners = self.driver.find_elements(*CARD_HEADER)
            cards = [card.find_element(*PARENT_CARD) for card in raid_banners]
        except NoSuchElementException:
            cards = []
        return cards

    def get_cards(self):
        """
        Get the list of cards on teh page

        :return: list of cards on the page
        """
        try:
            cards = self.driver.find_elements(*CARDS)
        except NoSuchElementException:
            cards = []
        return cards

    def get_list_titles(self):
        """
        Get the list of titles
        :return: list of titles
        """
        return self.driver.find_elements(*TITLES)

    def get_titles_for_cards(self, cards):
        """
        Get titles for the supplied list of cards
        :param cards: list of card webelements
        :return: list of titles from the cards
        """
        titles = []
        for card in cards:
            titles.append(self.get_title_for_card(card))
        return titles

    @staticmethod
    def get_title_for_card(card):
        """
        Get title for the supplied card
        :param card: Card Webelement
        :return: Card title
        """
        title = card.find_element(*CARD_CONTENT_TITLE)
        return title.text

    @staticmethod
    def card_has_raid_banner(card):
        """
        Verify that the gym card has the raid banner on it

        :param card: Card WebElement
        :return: True if raid banner present
        """
        try:
            card.find_element(*RAID_BANNER)
            return True
        except NoSuchElementException:
            return False

    @staticmethod
    def get_header_text_for_card(card):
        """
        Get header element for the supplied card
        :param card: Card webelement
        :return: Card header text
        """
        header = card.find_element(*CARD_HEADER)
        return header.text

    @staticmethod
    def get_card_by_title(cards, title):
        """
        Get card in card list by title
        :param cards: list of card webelements
        :param title: title to find
        :return: webelement
        """
        for card in cards:
            title_element = card.find_element(*CARD_CONTENT_TITLE)
            if title_element.text == title:
                return card

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
            if 'You still need to visit this gym' in date_str:
                dates.append(date_str)
            else:
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

    def get_search_bar(self):
        """
        Get the search bar
        :return: webelement for search bar
        """
        return self.driver.find_element(*SEARCH_BAR)

    def enter_search_term(self, term):
        """
        Enter a search term into search bar
        :param term: Search Term
        """
        search_bar = self.get_search_bar()
        search_bar.send_keys(term)
        time.sleep(2)

    def get_search_suggestions(self):
        """
        Get the suggestions from search
        :return: Get the dropdown list from search
        """
        return self.driver.find_elements(*SEARCH_SUGGESTIONS)

    def scroll_and_click(self, element):
        """
        Scroll so element is in view and click it

        :param element: Webelement to click
        """
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
