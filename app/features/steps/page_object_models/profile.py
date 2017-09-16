""" Page Object Model - Profile Page """
from .selectors.profile import PAGE_HEADER, RAID_LIST_TITLE, RAID_LIST_ITEMS, \
    RAID_LIST_ITEM_GYM, RAID_LIST_ITEM_DATE, RAID_LIST_ITEM_REMOVE
from .common import BasePage
from selenium.common.exceptions import NoSuchElementException


class ProfilePage(BasePage):
    """
    Page Object Model for User Profile Page
    """

    def get_page_header_text(self):
        """
        Get the text for page header
        :return: page header text
        """
        self.wait_for_element(PAGE_HEADER)
        header_element = self.driver.find_element(*PAGE_HEADER)
        return header_element.text

    def get_raid_list_header(self):
        """
        Get the raid list title
        :return: webelement for raid list title
        """
        self.wait_for_element(RAID_LIST_TITLE)
        return self.driver.find_element(*RAID_LIST_TITLE)

    def get_raid_list_items(self):
        """
        Get the table rows for the raid list
        :return: list of webelements for the raid table rows
        """
        items = []
        try:
            items = self.driver.find_elements(*RAID_LIST_ITEMS)
        except NoSuchElementException:
            pass
        return items

    @staticmethod
    def get_gym_for_raid(raid_item):
        """
        Get the gym in the table row for raid list
        :param raid_item: webelement for table row
        :return: text for Gym part of table
        """
        gym_name = raid_item.find_element(*RAID_LIST_ITEM_GYM)
        return gym_name.text

    @staticmethod
    def get_date_for_raid(raid_item):
        """
        Get the date in the table row for raid list
        :param raid_item: webelement for table row
        :return: text for Date part of table
        """
        date_col = raid_item.find_element(*RAID_LIST_ITEM_DATE)
        return date_col.text

    @staticmethod
    def get_remove_button_for_raid(raid_item):
        """
        Get the remove button in the table row for raid list
        :param raid_item: webelement for table row
        :return: text for Date part of table
        """
        return raid_item.find_element(*RAID_LIST_ITEM_REMOVE)

    @staticmethod
    def remove_raid_from_list(raid_item):
        """
        Press the remove button in the table for the raid
        :param raid_item: weblement for table row
        """
        button = raid_item.find_element(*RAID_LIST_ITEM_REMOVE)
        button.click()
