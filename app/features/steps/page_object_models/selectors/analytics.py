""" Selectors for profile page """
from selenium.webdriver.common.by import By

PAGE_HEADER = (By.CSS_SELECTOR, 'body > section.hero.is-bold h1')
OVERVIEW_STATS = (By.CSS_SELECTOR, 'nav.level > .level-item > div')
GYM_LIST_TITLE = (By.CSS_SELECTOR, '#top-gyms > h1')
GYM_LIST_TABLE = (By.CSS_SELECTOR, '#top-gyms > table')
LEVEL_LIST_TITLE = (By.CSS_SELECTOR, '#top-levels > h1')
LEVEL_LIST_TABLE = (By.CSS_SELECTOR, '#top-levels > table')
DAY_LIST_TITLE = (By.CSS_SELECTOR, '#top-days > h1')
DAY_LIST_TABLE = (By.CSS_SELECTOR, '#top-days > table')
HOUR_LIST_TITLE = (By.CSS_SELECTOR, '#top-hours > h1')
HOUR_LIST_TABLE = (By.CSS_SELECTOR, '#top-hours > table')
GYM_MAP = (By.ID, 'map')
TABLE_CONTENTS = (By.CSS_SELECTOR, 'tbody > tr td')
