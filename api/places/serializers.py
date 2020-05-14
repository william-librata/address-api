from rest_framework import serializers
from places.models import State
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'last_login']


class StateSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='state-detail', read_only=True, lookup_field='state_abbreviation')

    class Meta:
        model = State
        fields = ['url', 'state_pid', 'date_created', 'date_retired', 'state_name', 'state_abbreviation', 'created_by']
