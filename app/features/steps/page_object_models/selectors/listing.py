""" Selectors for list view """
from selenium.webdriver.common.by import By

TITLES = (By.CSS_SELECTOR, '.column.content > h1')
GYMS_TO_VISIT_CARDS = (
    By.CSS_SELECTOR,
    '#gyms_to_visit .columns > .column > .card'
)
COMPLETED_GYMS_CARDS = (
    By.CSS_SELECTOR,
    '#completed_gyms .columns > .column > .card'
)
CARDS = (By.CSS_SELECTOR, '.columns > .column > .card')
CARD_CONTENT = (By.CSS_SELECTOR, '.card-content')
CARD_CONTENT_TITLE = (By.CSS_SELECTOR, '.media-content > .title')
CARD_CONTENT_OSM_WAY = (
    By.CSS_SELECTOR,
    '.media-content > .title > i.fa.fa-tree'
)
CARD_CONTENT_EX_RAID = (
    By.CSS_SELECTOR,
    '.media-content > .title > i.fa.fa-ticket'
)
CARD_CONTENT_VISIT_DATE = (By.CSS_SELECTOR, '.content > p')
CARD_FOOTER = (By.CSS_SELECTOR, '.card-footer')
CARD_FOOTER_OPTION = (By.CSS_SELECTOR, '.card-footer-item')
PROGRESS_BAR = (By.CSS_SELECTOR, 'progress.progress')
PROGRESS_PERCENTAGE = (By.CSS_SELECTOR, '.hero-body h2.subtitle:last-child')
GYM_MANAGEMENT_LINK = (
    By.CSS_SELECTOR,
    '.hero-body h2.subtitle .is-primary.is-inverted'
)
SEARCH_BAR = (By.ID, 'gym-list-search-bar')
SEARCH_SUGGESTIONS = (
    By.CSS_SELECTOR,
    '#dropdown-menu .dropdown-content .dropdown-item'
)
CARD_HEADER = (By.CSS_SELECTOR, '.columns > .column > .card .raid-header')
RAID_BANNER = (By.CSS_SELECTOR, '.raid-header')
PARENT_CARD = (By.XPATH, '../../..')


def get_link_selector(button_name):
    """
    Create a selector for the button with the name
    :param button_name: Text on button
    :return: Selector tuple
    """
    return (By.LINK_TEXT, button_name)
