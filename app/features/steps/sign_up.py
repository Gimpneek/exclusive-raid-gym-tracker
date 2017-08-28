from behave import when, then
from page_object_models.forms import FormPage
from django.contrib.auth.models import User
from app.models.profile import Profile


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
