""" Selectors for profile page """
from selenium.webdriver.common.by import By

PAGE_HEADER = (By.CSS_SELECTOR, 'body > section.hero.is-bold h1')
RAID_LIST_TITLE = (By.CSS_SELECTOR, '#my-raids > h1')
RAID_LIST_TABLE = (By.CSS_SELECTOR, '#my-raids > table')
RAID_LIST_GYMS = (By.CSS_SELECTOR, '#my-raids tbody > tr td:first-child')
RAID_LIST_DATES = (By.CSS_SELECTOR, '#my-raids tbody > tr td:last-child')
RAID_LIST_ITEMS = (By.CSS_SELECTOR, '#my-raids tbody > tr')
RAID_LIST_ITEM_GYM = (By.XPATH, '//td[1]')
RAID_LIST_ITEM_DATE = (By.XPATH, '//td[2]')
RAID_LIST_ITEM_REMOVE = (By.XPATH, '//td[3]/a')
