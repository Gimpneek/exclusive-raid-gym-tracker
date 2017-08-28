""" Selectors for form view """
from selenium.webdriver.common.by import By

USERNAME_INPUT = (By.NAME, 'username')
PASSWORD_INPUT = (By.NAME, 'password')
SUBMIT_BUTTON = (By.ID, 'form_submit')
ERROR_MESSAGE = (By.CSS_SELECTOR, 'form > .notification')
