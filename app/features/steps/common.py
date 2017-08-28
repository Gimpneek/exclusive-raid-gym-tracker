from behave import given, when, then
from django.core.urlresolvers import reverse_lazy
from page_object_models.forms import FormPage


PAGE_MAPPING = {
    'sign up': 'signup',
    'login': 'login',
    'gym list': 'gym_list',
    'gym item': 'gym_item',
    'logout': 'logout'
}


ERROR_MESSAGE_MAPPING = {
    'asking them to enter a password': 'This field is required.',
    'telling them to use a different username':
        'A user with that username already exists.'
}


@given("the user visits the {page_to_visit} page")
@when("the user visits the {page_to_visit} page")
def visit_page(context, page_to_visit):
    """
    Look up and visit the defined page
    :param context: Behave context
    :param page_to_visit: Page to look up and get URL for
    """
    context.browser.get(
        context.base_url + str(reverse_lazy(PAGE_MAPPING.get(page_to_visit)))
    )


@then('the user is taken to the {page_to_check} page')
def verify_user_redirected(context, page_to_check):
    """
    Verify that the user is redirected to the defined page
    :param context: Behave context
    :param page_to_check: Page user should be have been taken to
    :return:
    """
    url = context.base_url + str(reverse_lazy(PAGE_MAPPING.get(page_to_check)))
    assert(context.browser.current_url == url)


@then('the user is shown an error message {message_intent}')
def verify_error_message(context, message_intent):
    """
    Verify error message is shown
    :param context: Behave context
    :param message_intent: Intent of the message
    :return:
    """
    form = FormPage(context.browser)
    assert(
        ERROR_MESSAGE_MAPPING.get(message_intent) in form.get_error_message())


@given('the user is logged in')
def log_user_in(context):
    """ Log the user in """
    context.browser.get(
        context.base_url + str(reverse_lazy(PAGE_MAPPING.get('login')))
    )
    form = FormPage(context.browser)
    form.enter_username('test_user')
    form.enter_password('password')
    form.submit_form()
