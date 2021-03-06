from behave import given, when, then
from app.models.gym_item import GymItem
from app.models.gym import Gym
from app.models.profile import Profile
from app.models.raid_item import RaidItem
from app.models.ex_raid_pokemon import ExRaidPokemon
from datetime import datetime, timedelta
from app.features.steps.page_object_models.listing import ListingPage
from app.features.steps.page_object_models.selectors.listing import \
    SEARCH_BAR
from app.features.steps.forms import enter_valid_date, press_submit_raid
from app.features.steps.common import get_url_from_name
import copy
import pytz


@given('the user has completed no raids')
def user_has_no_raids(context):
    """
    No need to set up raids for user
    :param context: Behave context
    """
    context.raid_count = 'none'


@given('the user has completed at least one raid')
def user_has_completed_raids(context):
    """
    Set up some completed raids for the user
    :param context: Behave context
    """
    context.raid_count = 'some'
    gyms = Gym.objects.all()
    profile = Profile.objects.get(pk=1)
    gym = gyms[0]
    GymItem.objects.create(
        gym=gym,
        profile=profile,
        gym_visit_date=datetime.now(tz=pytz.timezone('Europe/London'))
    )
    context.raid_gym = gym.name


@given('the user has completed all the raids being tracked')
def user_has_completed_all_raids(context):
    """
    Set up so user has all raids completed
    :param context: Behave context
    """
    context.raid_count = 'all'
    gyms = Gym.objects.all()
    profile = Profile.objects.get(pk=1)
    for gym in gyms:
        GymItem.objects.create(
            gym=gym,
            profile=profile,
            gym_visit_date=datetime.now(tz=pytz.timezone('Europe/London'))
        )


@then('they see a list of gyms they have yet to visit')
def get_yet_to_visit_gyms_list(context):
    """
    Get list of cards from the yet to visit list
    :param context: Behave context
    """
    page = ListingPage(context.browser)
    cards = page.get_yet_to_complete_cards()
    assert(len(cards) > 0)


@then('they see a list of gyms they have already visited')
def get_completed_gym_list(context):
    """
    Get list of cards from the completed gym list
    :param context: Behave context
    """
    page = ListingPage(context.browser)
    cards = page.get_completed_cards()
    assert(len(cards) > 0)


@then('they see a list of gyms with raids active')
@then('the user sees a list of raids that are currently happening')
def get_active_raid_list(context):
    """
    Get a list of cards from the active raids list
    :param context: Behave context
    """
    page = ListingPage(context.browser)
    cards = page.get_active_raid_cards()
    assert(len(cards) > 0)


@then('the list of gyms yet to visit is ordered alphabetically')
def check_alphabetically_order(context):
    """
    Get the list of titles and check it's ordered alphabetically
    :param context: Behave context
    """
    page = ListingPage(context.browser)
    cards = page.get_yet_to_complete_cards()
    titles = page.get_titles_for_cards(cards)
    sorted_titles = copy.deepcopy(titles)
    sorted_titles.sort()
    assert(titles == sorted_titles)


@then('the list of completed gyms is ordered so the oldest visits '
      'are at the top of the list')
def check_completed_gym_ordering(context):
    """
    Check the list of cards in the completed gym list is ordered correctly
    :param context:
    :return:
    """
    page = ListingPage(context.browser)
    cards = page.get_completed_cards()
    dates = page.get_visit_dates_for_cards(cards)
    sorted_dates = copy.deepcopy(dates)
    sorted_dates.sort()
    assert(dates == sorted_dates)


@then('the list and title for completed gyms is hidden')
def check_completed_raids_list_hidden(context):
    """
    Check that the completed raids title and list isn't in DOM
    :param context: Behave context
    """
    page = ListingPage(context.browser)
    titles = page.get_list_titles()
    cards = page.get_completed_cards()
    assert(len(titles) == 2)
    assert(len(cards) == 0)


@then('the list and title for yet to visit gyms is hidden')
def check_yet_to_visit_raids_list_hidden(context):
    """
    Check that the yet to visit raids title and list isn't in DOM
    :param context: Behave context
    """
    page = ListingPage(context.browser)
    titles = page.get_list_titles()
    cards = page.get_yet_to_complete_cards()
    assert(len(titles) == 2)
    assert(len(cards) == 0)


@then('the list and title for gyms with active raids is hidden')
def check_no_active_raids(context):
    """
    Check that the active raids title and list isn't in the DOM
    :param context: Behave context
    """
    page = ListingPage(context.browser)
    titles = page.get_list_titles()
    cards = page.get_active_raid_cards()
    assert(len(titles) == 2)
    assert(len(cards) == 0)


@when('they click on the {button_name} button on a gym card')
@given('they click on the {button_name} button on a gym card')
@given('the user presses the {button_name} button on a gym')
@when('the user presses the {button_name} button on a gym')
def click_gym_card_button(context, button_name):
    """
    Click on the defined button on the gym card
    :param context: Behave context
    :param button_name: name of the button
    """
    page = ListingPage(context.browser)
    if hasattr(context, 'active_raid_card'):
        cards = page.get_active_raid_cards()
    elif not hasattr(context, 'raid_count') or context.raid_count == 'none':
        cards = page.get_yet_to_complete_cards()
    else:
        cards = page.get_completed_cards()
    if hasattr(context, 'active_raid_card'):
        card = page.get_card_by_title(cards, context.active_raid_card)
    elif hasattr(context, 'past_raid_card'):
        card = page.get_card_by_title(cards, context.past_raid_card)
    else:
        card = cards[0]
    context.card_title = page.get_titles_for_cards([card])[0]
    context.card_text = page.get_visit_dates_for_cards([card])[0]
    button = page.get_card_button_by_name(card, button_name)
    context.card_url = button.get_attribute('href')
    page.scroll_and_click(button)


@then('the gym card is removed from the list')
def check_card_removed_from_list(context):
    """
    Check that the card is no longer in the list
    :param context: Behave context
    """
    page = ListingPage(context.browser)
    cards = page.get_yet_to_complete_cards()
    titles = page.get_titles_for_cards(cards)
    assert(context.card_title not in titles)


@then('the progress bar is updated to reflect the fact the '
      'gym is no longer counted')
def check_progress_bar_updated(context):
    """
    Check that the progress bar has been updated
    :param context: Behave context
    """
    page = ListingPage(context.browser)
    progress_bar = page.get_progress_bar()
    assert(progress_bar['max'] < context.progress_bar['max'])


@then('the progress bar will {completion_status}')
def check_progress_bar_empty(context, completion_status):
    """
    Check that the completion status of the progress bar is correct
    :param context: Behave context
    :param completion_status: Expected progress bar completion
    """
    page = ListingPage(context.browser)
    cards = page.get_completed_cards()
    progress_bar = page.get_progress_bar()
    value = progress_bar['value']
    if completion_status == 'be empty':
        assert(value == 0)
    elif completion_status == 'not be empty':
        assert(value > 0)
        assert(value < progress_bar['max'])
    elif completion_status == 'be full':
        assert(value == len(cards))
    else:
        raise NotImplementedError('Unexpected option')


@then('the completion percentage will {completion_status}')
def check_completion_percentage(context, completion_status):
    """
    Check the completion status of the percentage underneath the progress bar
    :param context: Behave context
    :param completion_status: Expected percentage value
    """
    page = ListingPage(context.browser)
    progress_bar = page.get_progress_bar()
    percentage = page.get_progress_percentage()
    if completion_status == 'be 0%':
        assert (percentage == 0)
    elif completion_status == 'reflect the completion percentage':
        assert ('{}%'.format(percentage) == progress_bar['percentage'])
    elif completion_status == 'be 100%':
        assert (percentage == 100)
    else:
        raise NotImplementedError('Unexpected option')


@then('the gym is present in the list of gyms {list_of_gyms}')
def check_gym_in_list(context, list_of_gyms):
    """
    Check that the gym in the correct list
    :param context: Behave context
    :param list_of_gyms: List card should be in
    """
    page = ListingPage(context.browser)
    if list_of_gyms == 'they have already visited':
        cards = page.get_completed_cards()
    elif list_of_gyms == 'they have yet to visit':
        cards = page.get_yet_to_complete_cards()
    else:
        raise NotImplementedError('Unexpected option')
    titles = page.get_titles_for_cards(cards)
    assert (context.card_title in titles)


@then('the gym card shows {text}')
def check_text_on_card(context, text):
    """
    Check the text on the card
    :param context: Behave context
    :param text: Text card should show
    """
    page = ListingPage(context.browser)
    cards = page.get_cards()
    card = page.get_card_by_title(cards, context.card_title)
    card_text = page.get_visit_dates_for_cards([card])[0]
    date_format = '%d-%m-%Y'
    if text == 'the date they entered as the last visited date':
        date_on_card = datetime.strptime(context.entered_date, date_format)
        assert(
            card_text.strftime(date_format) ==
            date_on_card.strftime(date_format)
        )
    if text == 'the unchanged visit date':
        date_on_card = context.card_text
        assert (
            card_text.strftime(date_format) ==
            date_on_card.strftime(date_format)
        )
    if text == 'they have yet to visit the gym':
        assert(card_text == 'You still need to visit this gym')


@then('They stay on the form')
def check_still_on_form(context):
    """
    Check that the user is still on the form
    :param context: Behave context
    """
    assert(context.browser.current_url == context.card_url)


@then('they should see a search bar')
def verify_search_bar_present(context):
    """
    Verify that the search bar is on the page
    :param context: Behave context
    """
    page = ListingPage(context.browser)
    assert(page.get_search_bar())


@when('they enter a {query_type} into the search input')
def enter_search_query(context, query_type):
    """
    Enter a query into the search bar
    :param context: Behave context
    :param query_type: partial match or no match
    """
    page = ListingPage(context.browser)
    if query_type == 'partial gym name':
        page.enter_search_term('Bri')
    if query_type == 'substring not found in any gym name':
        page.enter_search_term('Colin Wren Wrote This')


@when('they press the suggested gym')
def select_suggested_gym(context):
    """
    Select a gym in the suggested gyms
    :param context: Behave context
    """
    page = ListingPage(context.browser)
    suggestions = page.get_search_suggestions()
    option = None
    for suggestion in suggestions:
        if suggestion.text == 'Bridgewater Place':
            option = suggestion
    assert(option)
    context.card_url = option.get_attribute('href')
    page.click_and_verify_change(option, SEARCH_BAR, hidden=True)


@then('they should see a list of gyms that match that substring')
def get_suggestions(context):
    """
    Get the search suggestions
    :param context: Behave context
    """
    page = ListingPage(context.browser)
    assert(page.get_search_suggestions())


@then('they should see no gyms')
def verify_no_gyms(context):
    """
    Make sure no gyms shown
    :param context: Behave context
    """
    page = ListingPage(context.browser)
    assert(not page.get_search_suggestions())


@given('a raid is active on a gym')
def raid_is_active(context):
    """
    Set up a raid to be active on the gym
    :param context: Behave context
    """
    gym = Gym.objects.get(name=context.tracked_gym)
    raid = RaidItem.objects.create(
        gym=gym,
        pokemon='Mewtwo',
        level=5,
        end_date=datetime.now(tz=pytz.UTC) + timedelta(hours=1)
    )
    raid.save()
    context.active_raid_card = context.tracked_gym


@given('that gym is in a park')
def gym_is_in_park(context):
    """
    Set up the gym to be in a park

    :param context: Behave context
    """
    gym = Gym.objects.get(name=context.tracked_gym)
    gym.osm_way = 'leisure=park'
    gym.save()


@given("that gym has had an EX-Raid happen at it before")
def gym_has_had_ex_raid(context):
    """
    Set up the gym to have had an EX-Raid before

    :param context: Behave context
    """
    ex_pokemon = ExRaidPokemon.objects.create(name="Super Legendary Pokemon")
    ex_pokemon.save()
    gym = Gym.objects.get(name=context.tracked_gym)
    raid = RaidItem.objects.create(
        gym=gym,
        pokemon="Super Legendary Pokemon",
        level=5,
        end_date=datetime.now(tz=pytz.UTC) + timedelta(hours=1)
    )
    raid.save()


@given('a raid has happened on a gym')
def raid_has_happened(context):
    """
    Set up a raid in the past

    :param context: Behave context
    """
    gyms = Gym.objects.all()
    gym = gyms[0]
    raid = RaidItem.objects.create(
        gym=gym,
        pokemon='Mewtwo',
        level=5,
        end_date=datetime.now(tz=pytz.UTC) - timedelta(hours=3)
    )
    raid.save()
    context.past_raid_card = gym.name


@given('there has been no raids on a gym')
@given('there are no active raids')
def no_raids_active(context):
    """
    No raids should be active on the gym
    :param context: Behave context
    """
    pass


@then('they see a raid active banner on the gym\'s card')
def verify_raid_banner(context):
    """
    Verify that the Raid banner is shown

    :param context: Behave context
    """
    page = ListingPage(context.browser)
    cards = page.get_active_raid_cards()
    card = page.get_card_by_title(cards, context.active_raid_card)
    assert(page.card_has_raid_banner(card))


@then('they see a tree next to the gym name')
def verify_tree_in_title(context):
    """
    Verify that the tree icon indicating that the gym is in a park is on the
    card

    :param context: Behave context
    """
    page = ListingPage(context.browser)
    cards = page.get_cards()
    card = page.get_card_by_title(cards, context.tracked_gym)
    assert(page.card_has_tree(card))


@then('they see a ticket next to the gym name')
def verify_ticket_in_title(context):
    """
    Verify that the ticket icon indicating that the gym is in a park is on the
    card

    :param context: Behave context
    """
    page = ListingPage(context.browser)
    cards = page.get_cards()
    card = page.get_card_by_title(cards, context.tracked_gym)
    assert(page.card_has_ticket(card))


@then('the {field} of the raid pokemon is displayed')
def verify_raid_data(context, field):
    """
    Verify that the Raid fields are displayed correctly
    :param context: Behave context
    :param field: field to verify is shown
    """
    page = ListingPage(context.browser)
    cards = page.get_active_raid_cards()
    card = page.get_card_by_title(cards, context.active_raid_card)
    header = page.get_header_text_for_card(card)
    if field == 'name':
        assert('Mewtwo' in header)
    if field == 'level':
        assert('5' in header)
    if field == 'time remaining':
        assert('0:59:' in header)
        assert('remaining' in header)


@then('the gym is at the top of the yet to complete gym list')
def verify_raid_at_top(context):
    """
    Verify that the raid card is at the top of the list
    :param context: Behave context
    """
    page = ListingPage(context.browser)
    card = page.get_yet_to_complete_cards()[0]
    title = page.get_title_for_card(card)
    assert(title == context.active_raid_card)


@then('the user sees a link to the gym management page')
def verify_gym_management_link(context):
    """
    Assert that the link to the Gym Management page is present on the
    gym list page

    :param context: Behave context
    """
    page = ListingPage(context.browser)
    link = page.get_gym_management_link()
    assert link is not None


@when('the user completes a raid on a gym')
def complete_a_raid_on_gym_via_url(context):
    """
    Complete a raid on a gym via the UI

    :param context: Behave context to add gym name to
    """
    gyms = Gym.objects.all()
    gym = gyms[0]
    context.browser.get(get_url_from_name(context, 'add raid'))
    enter_valid_date(context)
    press_submit_raid(context)
    context.raid_gym = gym.name
