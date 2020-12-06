from rest_framework import serializers
from .models import Log


class CreateLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = ['LogContent', 'Installation']


class ViewLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = '__all__'
