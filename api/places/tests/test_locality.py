from django.test import TestCase
from rest_framework.test import APIClient

from places.models import Locality, State, GeocodeReliabilityAut, LocalityClassAut
from django.contrib.auth.models import User


class StateTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(username='api_user', email='api_user', password='password')

        GeocodeReliabilityAut.objects.create(code=1, name='GR_TEST_1', description='Geocode reliability test 1')

        LocalityClassAut.objects.create(code='1', name='LCA_TEST_1', description='Locality class test 1')

        State.objects.create(state_pid='TEST1', date_created='2020-06-01',
                             state_name='Test1 State', state_abbreviation='TS1')

        Locality.objects.create(locality_pid='TEST_LOCALITY_1', date_Created='2020-06-13',
                                locality_name='Test Locality 1', primary_postcode='1234',
                                gnaf_reliability_code=1, locality_class_code='1',
                                state_pid='TEST1')

        Locality.objects.create(locality_pid='TEST_LOCALITY_2', date_Created='2020-06-13',
                                locality_name='Test Locality 2', primary_postcode='5678',
                                gnaf_reliability_code=1, locality_class_code='1',
                                state_pid='TEST1')

    def test_locality_list_api(self):
        import pdb;pdb.set_trace()
        user = User.objects.get(username='api_user')
        client = APIClient()
        client.force_authenticate(user=user)
        response = client.get('/locality/')
        self.assertEqual(len(response.data['results']), 2)
        self.assertEqual(response.data['results'][0]['locality_name'], 'Test Locality 1')
        self.assertEqual(response.data['results'][1]['locality_name'], 'Test Locality 2')
        self.assertEqual(response.status_code, 200)

    def test_locality_list_api_not_authenticated(self):
        client = APIClient()
        response = client.get('/locality/')
        self.assertEqual(response.status_code, 403)

    def test_locality_detail_api(self):
        user = User.objects.get(username='api_user')
        client = APIClient()
        client.force_authenticate(user=user)
        response = client.get('/locality/TEST_LOCALITY_2/')
        self.assertEqual(response.data['locality_name'], 'Test Locality 1')
        self.assertEqual(response.status_code, 200)

    def test_locality_detail_api_not_authenticated(self):
        client = APIClient()
        response = client.get('/locality/TEST_LOCALITY_2/')
        self.assertEqual(response.status_code, 403)

    def test_locality_detail_api_not_exist(self):
        user = User.objects.get(username='api_user')
        client = APIClient()
        client.force_authenticate(user=user)
        response = client.get('/locality/TEST_LOCALITY_2/')
        self.assertEqual(response.status_code, 404)

