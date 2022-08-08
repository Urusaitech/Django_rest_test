from django.shortcuts import render
from rest_framework import viewsets

from serializers import ClientSerializer
from testmini.models import Client


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all().order_by('name')
    serializer_class = ClientSerializer