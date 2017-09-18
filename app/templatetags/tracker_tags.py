""" Template tags """
from django import template
from app.models.gym_item import GymItem
from app.models.profile import Profile


register = template.Library()


@register.simple_tag
def get_last_raid(gym, user):
    """
    Get the last raid for the gym by the user
    :param gym: app.models.Gym object
    :param user: app.models.User object
    :return: last raid date on the gym by the user
    """
    profile = Profile.objects.get(user__id=user)
    visit = GymItem.objects.filter(gym__id=gym, profile=profile).last()
    if visit:
        return visit.gym_visit_date
    return None
