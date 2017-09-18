""" Selectors for form view """
from selenium.webdriver.common.by import By

USERNAME_INPUT = (By.NAME, 'username')
PASSWORD_INPUT = (By.NAME, 'password')
GYM_VISIT_DATE_INPUT = (By.NAME, 'gym_visit_date')
SUBMIT_BUTTON = (By.ID, 'form_submit')
ERROR_MESSAGE = (By.CSS_SELECTOR, 'form > .notification')
CANCEL_BUTTON = (By.LINK_TEXT, 'Cancel')
REMOVE_RAID_BUTTON = (By.CSS_SELECTOR, '.message > .message-body .button')
