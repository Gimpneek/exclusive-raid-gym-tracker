from behave import given, when, then
from app.models.gym_item import GymItem
from datetime import date, datetime
from .page_object_models.listing import ListingPage
import copy


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
    gyms = GymItem.objects.all().filter(profile=1, hidden=False)
    gym = gyms[0]
    gym.last_visit_date = date.today()
    gym.save()


@given('the user has completed all the raids being tracked')
def user_has_completed_all_raids(context):
    """
    Set up so user has all raids completed
    :param context: Behave context
    """
    context.raid_count = 'all'
    gyms = GymItem.objects.all().filter(profile=1, hidden=False)
    for gym in gyms:
        gym.last_visit_date = date.today()
        gym.save()


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
    assert(len(titles) == 1)
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
    assert(len(titles) == 1)
    assert(len(cards) == 0)


@when('they click on the {button_name} button on a gym card')
@given('they click on the {button_name} button on a gym card')
def click_gym_card_button(context, button_name):
    """
    Click on the defined button on the gym card
    :param context: Behave context
    :param button_name: name of the button
    """
    page = ListingPage(context.browser)
    if not hasattr(context, 'raid_count') or context.raid_count == 'none':
        cards = page.get_yet_to_complete_cards()
    else:
        cards = page.get_completed_cards()
    context.progress_bar = page.get_progress_bar()
    card = cards[0]
    context.card_title = page.get_titles_for_cards([card])[0]
    context.card_text = page.get_visit_dates_for_cards([card])[0]
    button = page.get_card_button_by_name(card, button_name)
    context.card_url = button.get_attribute('href')
    button.click()


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
    if text == 'the date they entered as the last visited date':
        cards = page.get_completed_cards()
    else:
        cards = page.get_yet_to_complete_cards()
    card = page.get_card_by_title(cards, context.card_title)
    card_text = page.get_visit_dates_for_cards([card])[0]
    format = '%d-%m-%Y'
    if text == 'the date they entered as the last visited date':
        date_on_card = datetime.strptime(context.entered_date, format)
        assert(card_text.strftime(format) == date_on_card.strftime(format))
    if text == 'the unchanged visit date':
        date_on_card = context.card_text
        assert (card_text.strftime(format) == date_on_card.strftime(format))
    if text == 'they have yet to visit the gym':
        assert(card_text == 'You still need to visit this gym')


@then('They stay on the form')
def check_still_on_form(context):
    """
    Check that the user is still on the form
    :param context: Behave context
    """
    assert(context.browser.current_url == context.card_url)
