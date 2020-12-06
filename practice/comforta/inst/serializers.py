from rest_framework import serializers
from .models import Installation


class InstallationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Installation
        fields = ['name', 'description',
                  'serial_number', 'FirmwareVersion']


class InstallationViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Installation
        fields = '__all__'


class InstForCurrentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Installation
        fields = ['id', 'name', 'description',
                  'FirmwareVersion', 'DeviceMode', 'NetworkMode', 'LastCO2Value', 'NightModeEnabled', 'NightModeAuto', 'NightModeFrom', 'NightModeTo']


class UserEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Installation
        fields = ['id', 'name', 'description', 'DeviceMode', 'NetworkMode', 'LastCO2Value',
                  'NightModeEnabled', 'NightModeAuto', 'NightModeFrom', 'NightModeTo']
