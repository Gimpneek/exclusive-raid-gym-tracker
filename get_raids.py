import requests, pytz, os
from datetime import datetime
import django
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "exclusive_raid_tracker.settings"
)
django.setup()
from app.models.gym import Gym

params = {
    'by': 'leeds',
    'pokemon': 'false',
    'pokestops': 'false',
    'gyms': 'true',
    'scanned': 'false',
    'spawnpoints': 'false',
    'swLat': '53.794317',
    'swLng': '-1.534313',
    'neLat': '53.795159',
    'neLng': '-1.531268',
    'alwaysperfect': 'false',
    'raids': 'false'
}

raids = requests.get(os.environ.get('POGO_MAP_URL'), params=params)
gym_data = raids.json().get('gyms', {})

for gym_id, status in gym_data.items():
    raid_end = datetime.fromtimestamp(
        (status.get('raid_end_ms')/1000.0),
        tz=pytz.UTC
    )
    time_left = raid_end - datetime.now(tz=pytz.utc)
    if time_left.total_seconds() > 0:
        gym = Gym.objects.get(gym_hunter_id=gym_id)
        if gym:
            gym.raid_level = status.get('raid_level')
            gym.raid_pokemon = status.get('raid_pokemon_name')
            gym.raid_end_date = raid_end
            gym.save()
