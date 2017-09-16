""" Steps for Profile Page """
from datetime import date
from behave import then, when
from page_object_models.profile import ProfilePage


@then("the user's name is shown in the page header")
def assert_profile_header_text(context):
    """ Assert that the profile header text is the user's name """
    page = ProfilePage(context.browser)
    header_text = page.get_page_header_text()
    assert header_text == 'Profile: test_user'


@when("the user sees a list of their completed raids")
@then("the user sees a list of their completed raids")
def assert_raid_list_shown(context):
    """ Assert that profile shows list of completed raids """
    page = ProfilePage(context.browser)
    raid_header = page.get_raid_list_header()
    raid_list = page.get_raid_list_items()
    assert raid_header is not False
    assert len(raid_list) == 1


@then("the user sees a map of their completed raids")
def assert_raid_list_shown(context):
    """ Assert that profile shows map of completed raids """
    page = ProfilePage(context.browser)
    raid_map = page.get_raid_map()
    assert raid_map is not False


@then("the raid list shows the gym name")
def assert_list_item_name(context):
    """
    Assert that the name is in the raid list
    :param context: Behave Context
    """
    page = ProfilePage(context.browser)
    raid_list = page.get_raid_list_items()
    raid_gym = page.get_gym_for_raid(raid_list[0])
    assert raid_gym == context.raid_gym


@then("the raid list shows the visit date")
def assert_list_item_date(context):
    """
    Assert that the last_visit_date is shown in the raid list
    :param context: Behave context
    """
    page = ProfilePage(context.browser)
    raid_list = page.get_raid_list_items()
    raid_date = page.get_date_for_raid(raid_list[0])
    assert raid_date == date.today().strftime('%d/%m/%Y')


@then("the raid list shows a button remove the completed raid")
def assert_list_item_remove(context):
    """
    Assert there's a button to remove the completed raid
    :param context: Behave context
    """
    page = ProfilePage(context.browser)
    raid_list = page.get_raid_list_items()
    remove_button = page.get_remove_button_for_raid(raid_list[0])
    assert remove_button.text == 'Remove'


@when('the user presses the Remove Raid Data button')
def press_remove_raid(context):
    """
    Press the remove raid button
    :param context: Behave context
    """
    page = ProfilePage(context.browser)
    raid_list = page.get_raid_list_items()
    raid_item = raid_list[0]
    context.removed_raid_gym = page.get_gym_for_raid(raid_item)
    context.removed_raid_date = page.get_date_for_raid(raid_item)
    context.card_title = context.removed_raid_gym
    page.remove_raid_from_list(raid_item)


@then("the raid entry is no longer in the list of completed raids")
def assert_raid_removed(context):
    """
    Assert the raid is no longer in the list
    :param context: Behave context
    """
    page = ProfilePage(context.browser)
    raid_list = page.get_raid_list_items()
    for item in raid_list:
        assert page.get_gym_for_raid(item) != context.removed_raid_gym
        assert page.get_date_for_raid(item) != context.removed_raid_date
