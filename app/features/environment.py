from selenium import webdriver
import os


def after_scenario(context, scenario):
    context.browser.close()


def before_feature(context, feature):
    context.fixtures = ['gym-fixtures.json', 'test-fixtures.json']


def before_scenario(context, scenario):
    if os.environ.get('TRAVIS'):
        context.browser = webdriver.PhantomJS()
    else:
        context.browser = webdriver.Chrome()
    context.browser.get(context.base_url)
