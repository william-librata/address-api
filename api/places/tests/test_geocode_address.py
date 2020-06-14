from django.test import TestCase
from rest_framework.test import APIClient

from django.contrib.auth.models import User


class GeocodeAddressTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(username='api_user', email='api_user', password='password')

    def test_geocode_address_detail_api_not_authenticated(self):
        client = APIClient()
        response = client.get('/geocode/1 test street southbank 3006/')
        import pdb;pdb.set_trace()
        self.assertEqual(response.status_code, 403)

    '''
    def test_geocode_address_detail_api_not_exist(self):
        user = User.objects.get(username='api_user')
        client = APIClient()
        client.force_authenticate(user=user)
        response = client.get('/geocode/11 some garbage address southbank 3005/')
        self.assertEqual(response.status_code, 404)

    def test_geocodea_address_detail_api(self):
        user = User.objects.get(username='api_user')
        client = APIClient()
        client.force_authenticate(user=user)
        response = client.get('/geocode/1 test street southbank 3006/')
        self.assertEqual(response.data['state_abbreviation'], 'TS1')
    '''
