from backend.device.models import Os, Device
from rest_framework import serializers


class OsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Os
        fields = "__all__"

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = "__all__"
