from selenium import webdriver


def after_scenario(context, scenario):
    context.browser.close()


def before_all(context):
    context.fixtures = ['gym-fixtures.json', 'test-fixtures.json']


def before_scenario(context, scenario):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    context.browser = webdriver.Chrome(chrome_options=options)
