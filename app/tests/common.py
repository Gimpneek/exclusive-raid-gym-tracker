""" Helpful functions for testing """
from app.models.gym_item import GymItem
from app.models.gym import Gym
from app.models.profile import Profile
from django.contrib.auth.models import User


def create_gym_item(username=None, name=None, location=None, visit=None):
    """
    Create a Gym Item instance
    :param username: Username for User and Profile objects
    :param name: Name for the Gym
    :param location: Location for the Gym
    :param visit: Visit date for the visit
    :return: GymItem object
    """
    user = User.objects.create(username=username)
    profile = Profile.objects.create(
        user=user,
        pokemon_go_username=username
    )
    gym = Gym.objects.create(
        name=name,
        location=location
    )
    profile.tracked_gyms.add(gym)
    profile.save()
    gym_item = GymItem.objects.create(
        gym=gym,
        profile=profile,
        gym_visit_date=visit
    )
    return gym_item
