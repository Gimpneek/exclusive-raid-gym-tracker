from selenium import webdriver
import os


def after_scenario(context, scenario):
    print("Closing the browser now")
    context.browser.close()


def before_feature(context, feature):
    context.fixtures = ['gym-fixtures.json', 'test-fixtures.json']


def after_feature(context, feature):
    print("After the feature")


def before_scenario(context, scenario):
    options = webdriver.ChromeOptions()
    if os.environ.get('TRAVIS'):
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
    context.browser = webdriver.Chrome(chrome_options=options)
