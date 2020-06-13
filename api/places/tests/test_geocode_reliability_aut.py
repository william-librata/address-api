from django.test import TestCase
from rest_framework.test import APIClient

from places.models import GeocodeReliabilityAut
from django.contrib.auth.models import User


class GeocodeReliabilityAutTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(username='api_user', email='api_user', password='password')

        GeocodeReliabilityAut.objects.create(code=1, name='TEST1', description='Test geocode reliability aut 1')
        GeocodeReliabilityAut.objects.create(code=2, name='TEST2', description='Test geocode reliability aut 2')

    def test_geocode_reliability_aut_list_api(self):
        user = User.objects.get(username='api_user')
        client = APIClient()
        client.force_authenticate(user=user)
        response = client.get('/geocodereliabilityaut/')
        self.assertEqual(len(response.data['results']), 2)
        self.assertEqual(response.data['results'][0]['name'], 'TEST1')
        self.assertEqual(response.data['results'][1]['name'], 'TEST2')

    def test_geocode_reliability_aut_list_api_not_authenticated(self):
        client = APIClient()
        response = client.get('/geocodereliabilityaut/')
        self.assertEqual(response.status_code, 403)

    def test_geocode_reliability_aut_detail_api(self):
        user = User.objects.get(username='api_user')
        client = APIClient()
        client.force_authenticate(user=user)
        response = client.get('/geocodereliabilityaut/1/')
        self.assertEqual(response.data['name'], 'TEST1')

    def test_geocode_reliability_aut_detail_api_not_authenticated(self):
        client = APIClient()
        response = client.get('/geocodereliabilityaut/1/')
        self.assertEqual(response.status_code, 403)

    def test_geocode_reliability_aut_detail_api_not_exist(self):
        user = User.objects.get(username='api_user')
        client = APIClient()
        client.force_authenticate(user=user)
        response = client.get('/geocodereliability/9/')
        self.assertEqual(response.status_code, 404)

