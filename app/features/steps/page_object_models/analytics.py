""" Page Object Model - Analytics Page """
from .selectors.analytics import PAGE_HEADER, OVERVIEW_STATS, GYM_MAP, \
    GYM_LIST_TITLE, GYM_LIST_TABLE, LEVEL_LIST_TABLE, LEVEL_LIST_TITLE, \
    DAY_LIST_TABLE, DAY_LIST_TITLE, HOUR_LIST_TABLE, HOUR_LIST_TITLE, \
    TABLE_CONTENTS
from .common import BasePage


class AnalyticsPage(BasePage):
    """
    Page Object Model for Analytics Page
    """

    def get_page_header_text(self):
        """
        Get the text for page header
        :return: page header text
        """
        self.wait_for_element(PAGE_HEADER)
        header_element = self.driver.find_element(*PAGE_HEADER)
        return header_element.text

    def get_overview_stats(self):
        """
        Get the overview stats
        :return: webelements for overview stats
        """
        self.wait_for_element(OVERVIEW_STATS)
        return self.driver.find_elements(*OVERVIEW_STATS)

    def get_map(self):
        """
        Get the map for the active gyms
        :return: webelement for the map
        """
        self.wait_for_element(GYM_MAP)
        return self.driver.find_element(*GYM_MAP)

    def get_table_header(self, table_subject):
        """
        Get the header for the table based on the table subject

        :param table_subject: Name of the table
        :return: weblement for table title
        """
        header_selector = {
            'active gyms': GYM_LIST_TITLE,
            'raid levels': LEVEL_LIST_TITLE,
            'hours that raids happened in': DAY_LIST_TITLE,
            'days that raids happened on': HOUR_LIST_TITLE
        }
        self.wait_for_element(header_selector.get(table_subject))
        return self.driver.find_element(*header_selector.get(table_subject))

    def get_table(self, table_subject):
        """
        Get the table for the table based on the table subject

        :param table_subject: Name of the table
        :return: weblement for table title
        """
        table_selector = {
            'active gyms': GYM_LIST_TABLE,
            'raid levels': LEVEL_LIST_TABLE,
            'hours that raids happened in': DAY_LIST_TABLE,
            'days that raids happened on': HOUR_LIST_TABLE
        }
        self.wait_for_element(table_selector.get(table_subject))
        return self.driver.find_element(*table_selector.get(table_subject))

    @staticmethod
    def get_table_contents(table):
        """
        Get the contents of the table

        :param table: Table WebElement to get contents from
        :return: WebElement for table
        """
        return table.find_elements(*TABLE_CONTENTS)
