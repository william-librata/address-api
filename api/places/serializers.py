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


class LocalitySerializer(serializers.ModelSerializer):
    state_name = serializers.CharField(source='state_pid.state_name')
    locality_class_name = serializers.CharField(source='locality_class_code.name')
    geocode_reliability_name = serializers.CharField(source='gnaf_reliability_code.name')

    class Meta:
        model = Locality
        fields = ['locality_pid', 'locality_name', 'primary_postcode', 'state_pid',
                  'state_name', 'locality_class_code', 'locality_class_name',
                  'gnaf_reliability_code', 'geocode_reliability_name']


class LocalityClassAutSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LocalityClassAut
        fields = '__all__'


class GeocodeReliabilityAutSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GeocodeReliabilityAut
        fields = '__all__'
