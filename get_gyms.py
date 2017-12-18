import pytz, os, cfscrape
from datetime import datetime
import django
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "exclusive_raid_tracker.settings"
)
django.setup()
from app.models.gym import Gym
import json

with open('gyms.json') as gym_json:
    gym_data = json.load(gym_json)

    for gym in gym_data.get('gyms'):
        try:
            gym_obj = Gym.objects.get(name=gym.get('gym_name'))
        except Gym.DoesNotExist:
            name = gym.get('gym_name')
            location = '{lat},{lng}'.format(
                lat=gym.get('latitude'),
                lng=gym.get('longitude')
            )
            image = gym.get('gym_url')
            if all([name, location, image]):
                gym_obj = Gym.objects.create(
                    name=name,
                    location=location,
                    image_url=image
                )
