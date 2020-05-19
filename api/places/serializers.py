from rest_framework import serializers
from rest_framework.reverse import reverse
from places.models import State, Locality, LocalityClassAut, GeocodeReliabilityAut
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'last_login']


class StateSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='state-detail', read_only=True, lookup_field='state_pid')
    #created_by = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.select_related().only('username'))
    #created_by = serializers.ReadOnlyField(source='created_by.username', read_only=True)
    created_by = serializers.CharField(allow_null=True)

    class Meta:
        model = State
        fields = ['url', 'state_pid', 'date_created', 'date_retired', 'state_name', 'state_abbreviation', 'created_by']


class LocalitySerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='locality-detail', read_only=True, lookup_field='locality_pid')
    state_name = serializers.CharField(source='state_pid.state_name', allow_null=True)
    locality_class_name = serializers.CharField(source='locality_class_code.name', allow_null=True)
    geocode_reliability_name = serializers.CharField(source='gnaf_reliability_code.name', allow_null=True)
    state_pid = serializers.HyperlinkedRelatedField(view_name='state-detail', read_only=True, lookup_field='state_pid', allow_null=True)

    class Meta:
        model = Locality
        fields = ['url', 'locality_pid', 'locality_name', 'primary_postcode', 'state_pid',
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
