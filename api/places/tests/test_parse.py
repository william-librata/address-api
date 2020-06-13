from django.test import TestCase
from rest_framework.test import APIClient

from django.contrib.auth.models import User


class ParseTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(username='api_user', email='api_user', password='password')

    def test_parse_list_api_not_implemented(self):
        user = User.objects.get(username='api_user')
        client = APIClient()
        client.force_authenticate(user=user)
        response = client.get('/parse/')
        self.assertEqual(response.status_code, 404)

    def test_parse_detail_api_not_authenticated(self):
        client = APIClient()
        response = client.get('/parse/1 test street southbank 3006/')
        self.assertEqual(response.status_code, 403)

    def test_parse_detail_api_address_without_unit_number(self):
        user = User.objects.get(username='api_user')
        client = APIClient()
        client.force_authenticate(user=user)
        response = client.get('/parse/1 test street southbank 3006/')
        self.assertEqual(response.data['house'], None)
        self.assertEqual(response.data['category'], None)
        self.assertEqual(response.data['near'], None)
        self.assertEqual(response.data['house_number'], '1')
        self.assertEqual(response.data['road'], 'TEST STREET')
        self.assertEqual(response.data['unit'], None)
        self.assertEqual(response.data['level'], None)
        self.assertEqual(response.data['staircase'], None)
        self.assertEqual(response.data['entrance'], None)
        self.assertEqual(response.data['po_box'], None)
        self.assertEqual(response.data['postcode'], '3006')
        self.assertEqual(response.data['suburb'], None)
        self.assertEqual(response.data['city_district'], None)
        self.assertEqual(response.data['city'], 'SOUTHBANK')
        self.assertEqual(response.data['island'], None)
        self.assertEqual(response.data['state_district'], None)
        self.assertEqual(response.data['state'], None)
        self.assertEqual(response.data['country_region'], None)
        self.assertEqual(response.data['country'], None)
        self.assertEqual(response.data['world_region'], None)

    '''
    def test_parse_detail_api_address_with_unit_number(self):
        user = User.objects.get(username='api_user')
        client = APIClient()
        client.force_authenticate(user=user)
        response = client.get('/parse/', {'address': '1 test street southbank 3006'})
        import pdb;pdb.set_trace()
        self.assertEqual(response.data['house'], None)
        self.assertEqual(response.data['category'], None)
        self.assertEqual(response.data['near'], None)
        self.assertEqual(response.data['house_number'], '1')
        self.assertEqual(response.data['road'], 'TEST STREET')
        self.assertEqual(response.data['unit'], None)
        self.assertEqual(response.data['level'], None)
        self.assertEqual(response.data['staircase'], None)
        self.assertEqual(response.data['entrance'], None)
        self.assertEqual(response.data['po_box'], None)
        self.assertEqual(response.data['postcode'], '3006')
        self.assertEqual(response.data['suburb'], None)
        self.assertEqual(response.data['city_district'], None)
        self.assertEqual(response.data['city'], 'SOUTHBANK')
        self.assertEqual(response.data['island'], None)
        self.assertEqual(response.data['state_district'], None)
        self.assertEqual(response.data['state'], None)
        self.assertEqual(response.data['country_region'], None)
        self.assertEqual(response.data['country'], None)
        self.assertEqual(response.data['world_region'], None)
    '''