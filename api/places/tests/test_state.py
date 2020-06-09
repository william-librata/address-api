from django.test import TestCase
from rest_framework.test import APIClient

from places.models import State
from django.contrib.auth.models import User


class StateTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(username='api_user', email='api_user', password='password')

        State.objects.create(state_pid='TEST1', date_created='2020-06-01',
                             state_name='Test1 State', state_abbreviation='TS1')

        State.objects.create(state_pid='TEST2', date_created='2020-06-01',
                             state_name='Test2 State', state_abbreviation='TS2')

    def test_state_list_api(self):
        user = User.objects.get(username='api_user')

        client = APIClient()
        client.force_authenticate(user=user)

        response = client.get('/state/')

        self.assertEqual(len(response.data['results']), 2)
        self.assertEqual(response.data['results'][0]['state_abbreviation'], 'TS1')


