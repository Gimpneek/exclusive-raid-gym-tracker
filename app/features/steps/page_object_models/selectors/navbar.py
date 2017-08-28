""" Selectors for navbar """
from selenium.webdriver.common.by import By

SIGN_UP_BUTTON = (By.LINK_TEXT, 'Sign Up')
LOGIN_BUTTON = (By.LINK_TEXT, 'Login')
LOGOUT_BUTTON = (By.LINK_TEXT, 'Logout')
NAVBAR = (By.CSS_SELECTOR, 'nav.navbar')
