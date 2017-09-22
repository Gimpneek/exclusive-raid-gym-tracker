""" Common View Methods """


def create_js_obj_from_loc(loc):
    """
    Take a location and turn it into a JS object
    :param loc: location from raid
    :return: string representing JS object
    """
    raid_loc = loc.split(',')
    obj_str = '{'
    obj_str += 'lat: {0},lng: {1}'.format(raid_loc[0], raid_loc[1])
    obj_str += '}'
    return obj_str
