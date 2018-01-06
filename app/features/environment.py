from selenium import webdriver
import os


def after_scenario(context, scenario):
    context.browser.close()


def before_feature(context, feature):
    context.fixtures = ['gym-fixtures.json', 'test-fixtures.json']


def before_scenario(context, scenario):
    options = webdriver.ChromeOptions()
    if os.environ.get('TRAVIS'):
        options.add_argument('headless')
    context.browser = webdriver.Chrome(chrome_options=options)
