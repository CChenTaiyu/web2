from rest_framework import serializers
from weha.models import User, consumption_record


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ('id',
                  'username',
                  'password',
                  'balance',
                  'name')


class comsumptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = consumption_record
        fields = (
            'id',
            'Time',
            'Recipient',
            'Amount',
            'Money',
            'secret_key',
            'UserId',
            'Airline_order',
            'State')

