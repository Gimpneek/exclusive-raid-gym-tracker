import pytz
import os
import cfscrape
import json
from datetime import datetime
import django
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "exclusive_raid_tracker.settings"
)
django.setup()
from app.models.gym import Gym
from app.models.raid_item import RaidItem

new_params = {
    'type': 'raids',
    'area': 'leeds',
    'fields': 'all',
    'api-key': os.environ.get('GO_MAPS_KEY')
}


def resolve_dodgy_json(raw_resp):
    """
    Clean up the response from the server if it's not returning valid JSON

    :param raw_resp: Raw byte content from server response
    :return: JSON object
    """
    json_objects = raw_resp.decode('utf-8').split('{"success":')
    proper_json = '{"success":' + json_objects[2]
    return json.loads(proper_json).get('raids', {})


proxy_url = os.environ.get('QUOTAGUARDSTATIC_URL')
time_now = datetime.now(tz=pytz.timezone('Europe/London'))
if time_now.hour in range(6, 21):
    scraper = cfscrape.create_scraper()
    if proxy_url:
        proxies = {
            "http": proxy_url,
            "https": proxy_url
        }
        raids = scraper.post(
            os.environ.get('POGO_MAP_URL'),
            data=new_params,
            proxies=proxies
        )
    else:
        raids = scraper.post(os.environ.get('POGO_MAP_URL'), data=new_params)

    print("Status Code: {}".format(raids.status_code))
    if raids.status_code == 200:
        try:
            gym_data = raids.json().get('raids', {})
        except json.JSONDecodeError:
            print("Had to sort out JSON")
            print(raids.content.decode('utf-8'))
            gym_data = resolve_dodgy_json(raids.content)

        for status in gym_data:
            if status.get('raid_end_ms') and status.get('raid_level'):
                print("Found a raid")
                raid_end = datetime.fromtimestamp(
                    (status.get('raid_end_ms')/1000.0),
                    tz=pytz.UTC
                )
                now = datetime.now(tz=pytz.utc)
                time_left = raid_end - now
                if time_left.total_seconds() > 0:
                    print("The raid had some time left")
                    try:
                        gym = Gym.objects.get(gym_hunter_id=status.get('gym_id'))
                    except Gym.DoesNotExist:
                        gym = None
                    if gym:
                        print("Gym found: {}".format(gym.name))
                        raids = RaidItem.objects.filter(
                            gym=gym,
                            end_date=raid_end
                        )
                        if raids:
                            raid = raids[0]
                            raid.pokemon = status.get('raid_pokemon_name')
                            raid.save()
                        else:
                            RaidItem.objects.create(
                                gym=gym,
                                level=status.get('raid_level'),
                                pokemon=status.get('raid_pokemon_name'),
                                end_date=raid_end
                            )
