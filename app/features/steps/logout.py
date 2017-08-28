from behave import when, then
from page_object_models.common import BasePage
from common import get_url_from_name


@when('the user logs out of the system')
def log_user_out(context):
    """
    Log the user out of the system
    :param context: Behave context
    """
    page = BasePage(context.browser)
    page.press_logout()


@then('they cannot access the following pages')
def no_access_to_pages(context):
    """
    Check the user cannot access these pages
    :param context: Behave context
    """
    for item in context.table.rows:
        context.browser.get(get_url_from_name(context, item.cells[0]))
        assert('login' in context.browser.current_url)


@then('they can access the following pages')
def can_access_pages(context):
    """
    Check the user can access these pages
    :param context: Behave context
    """
    for item in context.table.rows:
        url = get_url_from_name(context, item.cells[0])
        context.browser.get(url)
        assert(context.browser.current_url == url)
