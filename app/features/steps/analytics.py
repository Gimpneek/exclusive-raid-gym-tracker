""" Steps for Analytics Page """
from calendar import day_name
from datetime import date, timedelta, datetime
from behave import then, given
from app.features.steps.page_object_models.analytics import AnalyticsPage
from app.models.raid_item import RaidItem
from app.models.gym import Gym
import pytz


@then("the analysis date range is shown in the page header")
def assert_analysis_header_text(context):
    """ Assert that the analytics header text is the user's name """
    page = AnalyticsPage(context.browser)
    header_text = page.get_page_header_text()
    now = datetime.combine(date.today(), datetime.min.time())
    one_week_ago = now + timedelta(weeks=-1)
    assert header_text == 'Analytics: {} - {}'.format(
        one_week_ago.strftime('%d/%m'),
        now.strftime('%d/%m')
    )


@given("at least {quantity} raid has popped up in the date period")
def create_raid_for_period(context, quantity):
    """
    Create a raid to appear in list for today
    :param context: Behave context
    :param quantity: Number of raids to set up (One, Ten)
    """
    now = datetime.combine(date.today(), datetime.min.time())
    if hasattr(context, 'tracked_gym'):
        gyms = [Gym.objects.get(name=context.tracked_gym)]
    else:
        if quantity == "one":
            gyms = [Gym.objects.all().last()]
        else:
            gyms = Gym.objects.all()[:11]
    for gym in gyms:
        RaidItem.objects.create(
            gym=gym,
            pokemon='MewTwo',
            level=5,
            end_date=now.replace(tzinfo=pytz.UTC)
        )
        context.most_active_gym = gym.name
    context.most_active_level = '5'
    context.most_active_day = day_name[now.weekday()]
    context.most_active_hour = str(datetime.min.time().hour)


@then("the user sees a count of the raids during the period")
def verify_shows_raid_count(context):
    """
    Verify that the count is shown in the header
    :param context: behave context
    """
    page = AnalyticsPage(context.browser)
    stats = page.get_overview_stats()
    assert('TOTAL RAIDS' in stats[0].text)
    assert('1' in stats[0].text)


@then("the user sees the name of the most active gym during the period")
def verify_shows_top_gym(context):
    """
    Verify that the most active gym is shown in the header
    :param context: behave context
    """
    page = AnalyticsPage(context.browser)
    stats = page.get_overview_stats()
    assert('GYM WITH MOST RAIDS' in stats[1].text)
    assert(context.most_active_gym in stats[1].text)


@then("the user sees the most active time of day during the period")
def verify_shows_top_hour(context):
    """
    Verify that the most active hour is shown in the header
    :param context: behave context
    """
    page = AnalyticsPage(context.browser)
    stats = page.get_overview_stats()
    assert('MOST ACTIVE HOUR' in stats[2].text)
    assert(context.most_active_hour in stats[2].text)


@then("the user sees a the most active day during the period")
def verify_shows_top_day(context):
    """
    Verify that the most active day is shown in the header
    :param context: behave context
    """
    page = AnalyticsPage(context.browser)
    stats = page.get_overview_stats()
    assert('MOST ACTIVE DAY' in stats[3].text)
    assert(context.most_active_day in stats[3].text)


@then("the user sees a map of the active gyms")
def assert_raid_map_shown(context):
    """ Assert that page shows map of most active gyms """
    page = AnalyticsPage(context.browser)
    raid_map = page.get_map()
    assert raid_map is not False


@then("the user sees a table of {table_subject}")
def assert_table_shown(context, table_subject):
    """ Assert table is shown
    :param context: Behave context
    :param table_subject: Subject for table
    """
    page = AnalyticsPage(context.browser)
    header = page.get_table_header(table_subject)
    table = page.get_table(table_subject)
    context.analytics_table = table
    assert header is not False
    assert table is not False


@then("only the ten most active gyms are shown in the table")
def assert_row_count(context):
    """
    Assert that only ten rows are shown in the active gym table

    :param context: Behave context
    """
    page = AnalyticsPage(context.browser)
    table = page.get_table('active gyms')
    contents = page.get_table_contents(table)
    assert len(contents) == 20
