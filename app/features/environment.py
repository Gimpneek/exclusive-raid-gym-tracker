from selenium import webdriver


def after_scenario(context, scenario):
    context.browser.close()


def before_all(context):
    context.fixtures = ['gym-fixtures.json', 'test-fixtures.json']


def before_feature(context, feature):
    print("Before the feature")


def before_scenario(context, scenario):
    print("about to create browser")
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    context.browser = webdriver.Chrome(chrome_options=options)
    print("Created browser")
