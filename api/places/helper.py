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

    def post_processing(result):
        # remove unit number from house number
        # if house number = '2 / 1', unit number is '2' and house number is '1'
        if '/' in result['house_number'] and len(result['house_number'].split('/')) == 2:
            unit, house_number = (r.strip() for r in result['house_number'].split('/'))
            result['house_number'] = house_number
            result['unit'] = (str(result['unit'] or '') + ' ' + unit).strip()

        # remove unit number and level from house number
        # if house number = '3/UNIT 2 / 1' and level = 'LEVEL', unit number is 'UNIT 2', level is 'LEVEL 3' and house number is '1'
        if '/' in result['house_number'] and len(result['house_number'].split('/')) == 3 and result['level'] == 'LEVEL':
            level, unit, house_number = (r.strip() for r in result['house_number'].split('/'))
            result['level'] = result['level'] + ' ' + level
            result['unit'] = (str(result['unit'] or '') + ' ' + unit).strip()
            result['house_number'] = house_number

        # remove unit number from house number
        # if house number = '2 1', unit number is '2' and house number is '1'
        if ' ' in result['house_number'] and len(result['house_number'].split(' ')) == 2:
            unit, house_number = (r.strip() for r in result['house_number'].split(' '))
            result['house_number'] = house_number
            result['unit'] = (str(result['unit'] or '') + ' ' + unit).strip()

        # move level number from unit number
        # if unit number = '1' and level = 'LEVEL', unit number is None and level number is 'LEVEL 1'
        if result['unit'] and result['level'] == 'LEVEL':
            result['level'] = result['level'] + ' ' + result['unit']
            result['unit'] = None

        return result

    # reverse named tuple
    result = dict((y, x.upper()) for x, y in postal_parse_address(address))

    # for every item in base schema, if corresponds with parsed_address, then get parsed_address value
    # else, get base_schema value which is None
    result = dict((k, result.get(k, get_parsed_address_schema().get(k))) for k, v in get_parsed_address_schema().items())

    # post processing
    result = post_processing(result)

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

    # check if there are enough info geocode address
    if parsed_address['suburb'] is None and \
       parsed_address['state'] is None and \
       parsed_address['postcode'] is None:
        raise NotEnoughInformation

    param = list(parsed_address.values())

    with connection.cursor() as cur:
        cur.callproc('geocode', param)
        result = dict_fetchone(cur)
    return result


class NotEnoughInformation(Exception):
    def __init__(self, message="Not enough information to geocode address. Add more details."):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message
