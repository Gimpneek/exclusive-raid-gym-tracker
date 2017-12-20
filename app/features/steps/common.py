from behave import given, when, then
from django.core.urlresolvers import reverse_lazy
from page_object_models.forms import FormPage
from app.models.profile import Profile
from app.models.gym import Gym


PAGE_MAPPING = {
    'sign up': 'signup',
    'login': 'login',
    'gym list': 'gym_list',
    'active raid list': 'raid_list',
    'add raid': ('add_gym_raid', {'gym_id': 1}),
    'logout': 'logout',
    'landing': 'index',
    'homepage': 'index',
    'analytics': 'analytics',
    'remove gym data url': ('remove_gym_item', {'gym_item_id': 1}),
    'hide gym in gym list url': ('hide_gym_item', {'gym_item_id': 1}),
    'user profile': 'profile',
    'gym management page': 'gym_management',
    'start tracking gym url': ('add_tracked_gym', {'gym_id': 1}),
    'stop tracking gym url': ('remove_tracked_gym', {'gym_id': 1})
}


ERROR_MESSAGE_MAPPING = {
    'asking them to enter a password': 'This field is required.',
    'telling them to use a different username':
        'A user with that username already exists.',
    'telling them no account exists for those credentials':
        'Unable to login with provided credentials',
    'saying the date is invalid': 'Invalid date entered'
}


def get_url_from_name(context, name):
    """ Get the URL to compare from the name supplied """
    name = name.lower()
    page = PAGE_MAPPING.get(name)
    if isinstance(page, tuple):
        return context.base_url + str(reverse_lazy(page[0], kwargs=page[1]))
    return context.base_url + str(reverse_lazy(page))


@given("the user visits the {page_to_visit} page")
@when("the user visits the {page_to_visit} page")
def visit_page(context, page_to_visit):
    """
    Look up and visit the defined page
    :param context: Behave context
    :param page_to_visit: Page to look up and get URL for
    """
    context.browser.get(get_url_from_name(context, page_to_visit))


@then('the user is taken to the {page_to_check} page')
@when('the user is taken to the {page_to_check} page')
@given('the user is taken to the {page_to_check} page')
def verify_user_redirected(context, page_to_check):
    """
    Verify that the user is redirected to the defined page
    :param context: Behave context
    :param page_to_check: Page user should be have been taken to
    :return:
    """
    url = get_url_from_name(context, page_to_check)
    if hasattr(context, 'card_url') and context.card_url:
        url = context.card_url
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
    context.browser.get(get_url_from_name(context, 'login'))
    form = FormPage(context.browser)
    form.enter_username('test_user')
    form.enter_password('password')
    form.submit_form()


@then('a user session is created')
def verify_user_session(context):
    """
    Verify that the user has a session created for them

    :param context: Behave context
    """
    assert(context.browser.get_cookie('sessionid') is not None)


@then('the user session is ended')
def verify_user_session_ended(context):
    """
    Verify that the user has a session created for them

    :param context: Behave context
    """
    assert(context.browser.get_cookie('sessionid') is None)


@given('the user is tracking at least one gym')
def user_tracks_gym(context):
    """
    Set up the user to be tracking a gym

    :param context: Behave context
    """
    profile = Profile.objects.all()[0]
    gym = Gym.objects.all()[0]
    profile.tracked_gyms.add(gym)
    profile.save()
    context.tracked_gym = gym.name
