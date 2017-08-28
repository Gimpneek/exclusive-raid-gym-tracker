from behave import given, when, then
from page_object_models.forms import FormPage


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
    :param input:
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
