from django.test import TestCase
from rest_framework.test import APIClient

from places.models import Address
from django.contrib.auth.models import User


class GeocodeAddressTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(username='api_user', email='api_user', password='password')

        Address.objects.create(address_detail_pid='ADDRESS1', building_name='BUILDING 1', lot_number_combined=None,
                               flat_number_combined=None, level_number_combined=None, house_number='11-13',
                               number_first_combined='11', number_last_combined='13',
                               street_name='TEST', street_type='ROAD', street_suffix_code='W', street_suffix_name='WEST',
                               street='TEST ROAD W', locality_name='RICHMOND', state='VIC', postcode='3000',
                               latitude=1.123, longitude=120)

        Address.objects.create(address_detail_pid='ADDRESS2', building_name='BUILDING 2', lot_number_combined='LOT 1',
                               flat_number_combined='UNIT 1', level_number_combined='LEVEL 1', house_number='20',
                               street_name='TEST', street_type='ROAD', street_suffix_code='W', street_suffix_name='WEST',
                               street='TEST ROAD W', locality_name='RICHMOND', state='VIC', postcode='3000',
                               latitude=1.123, longitude=120)

    def test_geocode_address_api_not_authenticated(self):
        client = APIClient()
        response = client.get('/geocode/1 test street southbank 3006/')
        self.assertEqual(response.status_code, 403)

    def test_geocode_address_api_not_exist(self):
        user = User.objects.get(username='api_user')
        client = APIClient()
        client.force_authenticate(user=user)
        response = client.get('/geocode/11 some garbage address southbank 3005/')
        self.assertEqual(response.status_code, 404)

    def test_geocode_address_api_address_without_unit_number(self):
        user = User.objects.get(username='api_user')
        client = APIClient()
        client.force_authenticate(user=user)
        response = client.get('/geocode/11 test rd richmond 3000/')
        self.assertEqual(response.data['address_detail_pid'], 'ADDRESS1')

    def test_geocode_address_api_address_with_unit_number(self):
        user = User.objects.get(username='api_user')
        client = APIClient()
        client.force_authenticate(user=user)
        response = client.get('/geocode/unit 1/20 test rd richmond 3000/')
        self.assertEqual(response.data['address_detail_pid'], 'ADDRESS2')
