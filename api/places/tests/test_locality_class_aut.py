from django.test import TestCase
from rest_framework.test import APIClient

from places.models import LocalityClassAut
from django.contrib.auth.models import User


class LocalityClassAutTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(username='api_user', email='api_user', password='password')

        LocalityClassAut.objects.create(code='A', name='TEST1', description='Test locality aut 1')
        LocalityClassAut.objects.create(code='B', name='TEST2', description='Test locality aut 2')

    def test_locality_class_aut_list_api(self):
        user = User.objects.get(username='api_user')
        client = APIClient()
        client.force_authenticate(user=user)
        response = client.get('/localityclassaut/')
        self.assertEqual(len(response.data['results']), 2)
        self.assertEqual(response.data['results'][0]['name'], 'TEST1')
        self.assertEqual(response.data['results'][1]['name'], 'TEST2')

    def test_locality_class_aut_list_api_not_authenticated(self):
        client = APIClient()
        response = client.get('/localityclassaut/')
        self.assertEqual(response.status_code, 403)

    def test_locality_class_aut_detail_api(self):
        user = User.objects.get(username='api_user')
        client = APIClient()
        client.force_authenticate(user=user)
        response = client.get('/localityclassaut/A/')
        self.assertEqual(response.data['name'], 'TEST1')

    def test_locality_class_aut_detail_api_not_authenticated(self):
        client = APIClient()
        response = client.get('/localityclassaut/A/')
        self.assertEqual(response.status_code, 403)

    def test_locality_class_aut_detail_api_not_exist(self):
        user = User.objects.get(username='api_user')
        client = APIClient()
        client.force_authenticate(user=user)
        response = client.get('/localityclassaut/Z/')
        self.assertEqual(response.status_code, 404)

