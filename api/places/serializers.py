from rest_framework import serializers
from places.models import State

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ['state_pid', 'date_created', 'date_retired', 'state_name', 'state_abbreviation']
