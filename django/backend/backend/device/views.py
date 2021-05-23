from django.shortcuts import render
from rest_framework import viewsets
from backend.device.serializers import OsSerializer, DeviceSerializer
from backend.device.models import Os, Device

# Create your views here.

class OsViewSet(viewsets.ModelViewSet):
    queryset = Os.objects.all().order_by('-pub_date')
    serializer_class = OsSerializer

class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
