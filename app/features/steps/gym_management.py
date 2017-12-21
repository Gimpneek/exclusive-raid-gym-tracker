from behave import when, then
from django.contrib.auth.models import User
from app.features.steps.page_object_models.gym_management import \
    GymManagementPage
from app.models.profile import Profile
from app.models.gym import Gym


@when('the user presses the Remove Gym button on a gym in the table')
def remove_gym_via_table(context):
    """
    Stop tracking the gym set in the context from the table of tracked gyms by
    pressing the remove button in the table

    :param context: Behave context
    """
    page = GymManagementPage(context.browser)
    gym_row = page.find_tracked_gym(context.tracked_gym)
    page.remove_tracked_gym(gym_row)


@then('the user stops tracking that gym')
def verify_no_longer_tracking_gym(context):
    """
    Assert that the gym that was being tracked is no longer being tracked

    :param context: Behave context
    """
    user = User.objects.get(username='test_user')
    profile = Profile.objects.get(user=user)
    gyms = [gym.name for gym in profile.tracked_gyms.all()]
    assert context.tracked_gym not in gyms


@then('the user starts tracking that gym')
def verify_following_gym(context):
    """
    Assert that the gym in the context is being tracked

    :param context:
    """
    user = User.objects.get(username='test_user')
    profile = Profile.objects.get(user=user)
    gyms = [gym.name for gym in profile.tracked_gyms.all()]
    if hasattr(context, 'raid_gym'):
        assert context.raid_gym in gyms
    if hasattr(context, 'gym_to_track'):
        assert context.gym_to_track in gyms


@when('the user enters the name of a gym into the search bar')
def enter_gym_name_in_search_bar(context):
    """
    Enter the name of a gym into the search bar

    :param context: Behave context to put name of gym into
    """
    gym = Gym.objects.all().first()
    page = GymManagementPage(context.browser)
    page.enter_search_term(gym.name)
    context.gym_to_track = gym.name


@when('the user presses the suggested gym')
def select_suggested_gym(context):
    """
    Select a gym in the suggested gyms in the search bar

    :param context: Behave context to get name of gym from
    """
    page = GymManagementPage(context.browser)
    page.press_suggested_gym(context.gym_to_track)
