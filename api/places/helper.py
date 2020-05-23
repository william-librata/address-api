from postal.parser import parse_address as postal_parse_address
from django.db import connection

def get_address_schema():
    return {
            'address_id': None,
            'house': None,
            'category': None,
            'near': None,
            'house_number': None,
            'road': None,
            'unit': None,
            'level': None,
            'staircase': None,
            'entrance': None,
            'po_box': None,
            'postcode': None,
            'suburb': None,
            'city_district': None,
            'city': None,
            'island': None,
            'state_district': None,
            'state': None,
            'country_region': None,
            'country': None,
            'world_region': None,
            'latitude': None,
            'longitude': None
    }


def parse_address(address):
    # reverse named tuple
    result = dict((y, x) for x, y in postal_parse_address(address))

    # for every item in base schema, if corresponds with parsed_address, then get parsed_address value
    # else, get base_schema value which is None
    result = dict((k, result.get(k, get_address_schema().get(k))) for k, v in get_address_schema().items())
    return result


def geocode_address(address):
    parsed_address = parse_address(address)
    cursor = connection.cursor()
    result = cursor.callproc('geocode', [parsed_address]).fetchall()
    return result

