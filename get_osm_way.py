import os
import django
import math
import overpy
import progressbar

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "exclusive_raid_tracker.settings"
)
django.setup()
from app.models.gym import Gym


def deg2num(lat_deg, lon_deg, zoom):
    """
    Using the zoom level calculate the tile coords for the provided latitude
    and longitude

    :param lat_deg: The latitude of the location
    :param lon_deg: The longitude of the location
    :param zoom: The zoom level for the tile
    :return: tuple of the of the tile coords
    """
    lat_rad = math.radians(lat_deg)
    n = 2.0 ** zoom
    xtile = int((lon_deg + 180.0) / 360.0 * n)
    ytile = int(
        (1.0 - math.log(math.tan(lat_rad) + (1 / math.cos(lat_rad)))
         / math.pi) / 2.0 * n
    )
    return xtile, ytile


def num2deg(xtile, ytile, zoom):
    """
    Calculate the location from the tile coordinates at the given zoom level

    :param xtile: The tile's X coord
    :param ytile: The tile's Y coord
    :param zoom: the zoom level at which to calculate at
    :return: tuple of latitude and longitude
    """
    n = 2.0 ** zoom
    lon_deg = xtile / n * 360.0 - 180.0
    lat_rad = math.atan(math.sinh(math.pi * (1 - 2 * ytile / n)))
    lat_deg = math.degrees(lat_rad)
    return lat_deg, lon_deg


ZOOM = 19
SEARCH_DIST = 20
gyms = Gym.objects.all()
api = overpy.Overpass()
bar = progressbar.ProgressBar()


for gym in bar(gyms):
    lat, lng = [float(val) for val in gym.location.split(',')]
    tile_x, tile_y = deg2num(lat, lng, ZOOM)
    bounding_box = (
        *num2deg(tile_x+1, tile_y+1, ZOOM),
        *num2deg(tile_x, tile_y, ZOOM)
    )
    result = api.query(
        """
        [timeout:10][out:json];
        (
            way(around:{search_dist},{lat},{lng})["leisure"]);
            out tags geom{bounding_box};
        """.format(
            search_dist=SEARCH_DIST,
            lat=lat,
            lng=lng,
            bounding_box=bounding_box
        )
    )
    if result.way_ids:
        gym.osm_way = "leisure={}".format(result.ways[0].tags.get('leisure'))
        gym.save()
