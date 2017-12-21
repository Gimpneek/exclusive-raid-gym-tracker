""" Selectors for gym management page """
from selenium.webdriver.common.by import By

TRACKED_GYMS_TABLE = (By.CSS_SELECTOR, '#tracked-gyms > table')
TRACKED_GYMS_TABLE_ROW = (
    By.CSS_SELECTOR,
    '#tracked-gyms > table > tbody > tr'
)
TABLE_COLUMNS = (By.CSS_SELECTOR, 'td')
REMOVE_BUTTON = (By.CSS_SELECTOR, 'a')
