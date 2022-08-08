from rest_framework import serializers

from testmini.models import Client


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ('name', 'company', 'client_id', 'sum', 'date', 'service')

