from postal.parser import parse_address as postal_parse_address
from psycopg2.extras import RealDictCursor
from django.db import connection

def get_parsed_address_schema():
    return {
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
            'world_region': None
    }

def get_geocode_result_schema():
    return {
            'address_detail_pid': None,
            'latitude': None,
            'longitude': None
    }

def parse_address(address):
    # reverse named tuple
    result = dict((y, x.upper()) for x, y in postal_parse_address(address))

    # for every item in base schema, if corresponds with parsed_address, then get parsed_address value
    # else, get base_schema value which is None
    result = dict((k, result.get(k, get_parsed_address_schema().get(k))) for k, v in get_parsed_address_schema().items())
    return result


def dict_fetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def dict_fetchone(cursor):
    "Return single rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    row = cursor.fetchone()
    return dict(zip(columns, row))


def geocode_address(address):
    parsed_address = parse_address(address)
    param = list(parsed_address.values())

    with connection.cursor() as cur:
        cur.callproc('geocode', param)
        result = dict_fetchone(cur)
    return result

