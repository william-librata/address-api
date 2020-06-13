from django.test import TestCase
from rest_framework.test import APIClient

from places.models import Address
from django.contrib.auth.models import User


class AddressTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(username='api_user', email='api_user', password='password')

        Address.objects.create(address_detail_pid='ADDRESS1', building_name='BUILDING 1', lot_number_combined='LOT 1',
                               flat_number_combined='UNIT 1', level_number_combined='LEVEL 1', house_number='11-13',
                               street_name='TEST', street_type='ROAD', street_suffix_code='W', street_suffix_name='WEST',
                               street='TEST ROAD W', locality_name='RICHMOND', state='VIC', postcode='3000',
                               latitude=1.123, longitude=120)

    def test_address_list_api(self):
        user = User.objects.get(username='api_user')
        client = APIClient()
        client.force_authenticate(user=user)
        response = client.get('/address/')
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['street'], 'TEST ROAD W')
        self.assertEqual(response.data['results'][0]['latitude'], '1.12300000')
        self.assertEqual(response.data['results'][0]['longitude'], '120.00000000')

    def test_address_list_api_not_authenticated(self):
        client = APIClient()
        response = client.get('/address/')
        self.assertEqual(response.status_code, 403)

    def test_address_detail_api(self):
        user = User.objects.get(username='api_user')
        client = APIClient()
        client.force_authenticate(user=user)
        response = client.get('/address/ADDRESS1/')
        self.assertEqual(response.data['street'], 'TEST ROAD W')
        self.assertEqual(response.data['latitude'], '1.12300000')
        self.assertEqual(response.data['longitude'], '120.00000000')

    def test_address_detail_api_not_authenticated(self):
        client = APIClient()
        response = client.get('/address/ADDRESS1/')
        self.assertEqual(response.status_code, 403)

    def test_address_detail_api_not_exist(self):
        user = User.objects.get(username='api_user')
        client = APIClient()
        client.force_authenticate(user=user)
        response = client.get('/address/ADDRESS100/')
        self.assertEqual(response.status_code, 404)

