from django.test import TestCase
from rest_framework.test import APIClient

from django.contrib.auth.models import User


class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(username='api_user', email='api_user@user.com', password='password')
        User.objects.create_user(username='other_user', email='other_user@user.com', password='password')
        User.objects.create_user(username='another_user', email='another_user@user.com', password='password')

    def test_user_list_api(self):
        user = User.objects.get(username='api_user')
        client = APIClient()
        client.force_authenticate(user=user)
        response = client.get('/user/')
        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.data[0]['username'], 'api_user')
        self.assertEqual(response.data[1]['username'], 'other_user')
        self.assertEqual(response.data[2]['username'], 'another_user')

    def test_user_list_api_not_authenticated(self):
        client = APIClient()
        response = client.get('/user/')
        self.assertEqual(response.status_code, 403)

    def test_user_detail_api(self):
        user = User.objects.get(username='api_user')
        client = APIClient()
        client.force_authenticate(user=user)
        response = client.get('/user/another_user/')
        self.assertEqual(response.data['email'], 'another_user@user.com')

    def test_user_detail_api_not_authenticated(self):
        client = APIClient()
        response = client.get('/user/other_user/')
        self.assertEqual(response.status_code, 403)

    def test_user_detail_api_not_exist(self):
        user = User.objects.get(username='api_user')
        client = APIClient()
        client.force_authenticate(user=user)
        response = client.get('/state/some_user/')
        self.assertEqual(response.status_code, 404)

