import pytz, os, cfscrape, time, re
from datetime import datetime
import django
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "exclusive_raid_tracker.settings"
)
django.setup()

from app.models.gym import Gym
from app.models.raid_item import RaidItem

params = {
    'by': 'leeds',
    'excluded': '',
    'pokemon': 'false',
    'pokestops': 'false',
    'gyms': 'true',
    'scanned': 'false',
    'spawnpoints': 'false',
    'swLat': '53.64565540685835',
    'swLng': '-2.061996459960938',
    'neLat': '53.877226052392416',
    'neLng': '-0.9084320068359376',
    'alwaysperfect': '1',
    'raids': 'false',
    'token': '',
    'time': int(time.time())
}


proxy_url = os.environ.get('QUOTAGUARDSTATIC_URL')

time_now = datetime.now(tz=pytz.timezone('Europe/London'))

if time_now.hour in range(6, 21):
    scraper = cfscrape.create_scraper()
    if proxy_url:
        proxies = {
            "http": proxy_url,
            "https": proxy_url
        }
        raids = scraper.get(
            os.environ.get('POGO_MAP_URL'),
            params=params,
            proxies=proxies
        )
    else:
        page = scraper.get(os.environ.get('POGO_INITIAL_URL'))
        token_regex = re.compile(r'.*var token = \"([a-z0-9]+)\";')
        token = token_regex.match(str(page.content)).groups()[0]
        params['token'] = token
        raids = scraper.get(os.environ.get('POGO_MAP_URL'), params=params)

    if raids.status_code == 200:
        gym_data = raids.json().get('gyms', {})

        for status in gym_data:
            if status.get('raid_end_ms') and status.get('raid_level'):
                raid_end = datetime.fromtimestamp(
                    (status.get('raid_end_ms')/1000.0),
                    tz=pytz.UTC
                )
                now = datetime.now(tz=pytz.utc)
                time_left = raid_end - now
                if time_left.total_seconds() > 0:
                    try:
                        gym = Gym.objects.get(name=status.get('gym_name'))
                    except Gym.DoesNotExist:
                        gym = None
                    if gym:
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
