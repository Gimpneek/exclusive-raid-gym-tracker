from behave import given, when, then
from page_object_models.forms import FormPage
from django.contrib.auth.models import User
from app.models.profile import Profile
from datetime import datetime


@when('the user enters a username not currently in the system')
def enter_new_username(context):
    """
    Enter username that exists or doesn't exists in the system
    :param context: Behave context
    """
    form = FormPage(context.browser)
    form.enter_username('new_user')


@when('the user enters a username currently in the system')
def enter_existing_username(context):
    """
    Enter username that exists or doesn't exists in the system
    :param context: Behave context
    """
    form = FormPage(context.browser)
    form.enter_username('test_user')


@when('the user enters a password')
def enter_password(context):
    """
    Enter password for user
    :param context:
    :return:
    """
    form = FormPage(context.browser)
    form.enter_password('password')


@when('the user doesn\'t enter a password')
def dont_enter_password(context):
    """
    Don't enter a password
    :param context:
    :return:
    """
    pass


@when('the user presses the submit button')
def submit_form(context):
    """
    Submit the form
    :param context:
    :return:
    """
    form = FormPage(context.browser)
    if 'form-errors' in context.scenario.tags:
        form.submit_form(expect_error=True)
    else:
        form.submit_form()


@then('an account is created in the system for the user')
def verify_account_created(context):
    """
    Verify that the user account is created
    :param context:
    :return:
    """
    users = User.objects.all().count()
    profiles = Profile.objects.all().count()
    assert(users == 2)
    assert(profiles == 2)


@given('the user doesn\'t have an account in the system')
def user_doesnt_have_account(context):
    """
    User has an account in system
    :param context:
    :return:
    """
    pass


@given('the user has an account in the system')
def user_has_account(context):
    """
    User has an account in system
    :param context:
    :return:
    """
    pass


@when('the user enters the password for the username')
def enter_password_for_account(context):
    """
    Enter the password for the account
    :param context:
    :return:
    """
    form = FormPage(context.browser)
    form.enter_password('password')


@when('there is a typo in the {input_name}')
def typo_in_input(context, input_name):
    """
    Add a typo to the input
    :param context:
    :param input_name:
    :return:
    """
    form = FormPage(context.browser)
    if input_name == 'username':
        form.enter_username('typo')
    if input_name == 'password':
        form.enter_password('typo')


@then('the user is logged in')
def user_is_logged_in(context):
    """
    User is logged in
    :param context:
    :return:
    """
    pass


@when('the user presses the Submit Raid button')
def press_submit_raid(context):
    """
    Press the remove raid button
    :param context: Behave context
    """
    form = FormPage(context.browser)
    form.submit_form()
    context.card_url = None


@when('the user presses the Cancel button')
def press_cancel_button(context):
    """
    Press the cancel button
    :param context: Behave context
    """
    form = FormPage(context.browser)
    form.cancel_form()
    context.card_url = None


@when('they enter {validity} date into the last raid visit entry box')
def enter_valid_date(context, validity):
    """
    Enter valid date into the last visit date input
    :param context: Behave context
    :param validity: Is date valid?
    """
    today = datetime.now().strftime('%d-%m-%Y')
    context.entered_date = today
    # if context.browser.capabilities.get('browserName') == 'phantomjs':
    #     today = datetime.today().strftime('%Y-%m-%dT%H:%M')
    # form = FormPage(context.browser)
    # form.enter_gym_visit_date(today)
