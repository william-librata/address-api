from rest_framework import serializers
from places.models import State, Locality, LocalityClassAut, GeocodeReliabilityAut
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'last_login']


class StateSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='state-detail', read_only=True, lookup_field='state_pid')

    class Meta:
        model = State
        fields = ['url', 'state_pid', 'date_created', 'date_retired', 'state_name', 'state_abbreviation', 'created_by']


class LocalitySerializer(serializers.HyperlinkedModelSerializer):
    state_pid = serializers.HyperlinkedRelatedField(view_name='state-detail', read_only=True, lookup_field='state_pid')

    class Meta:
        model = Locality
        fields = '__all__'


class LocalityClassAutSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LocalityClassAut
        fields = '__all__'


class GeocodeReliabilityAutSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GeocodeReliabilityAut
        fields = '__all__'
