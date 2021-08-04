from rest_framework import serializers
from .models import Employed, Sede

class EmployedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employed
        fields = ['all']

class SedeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sede
        fields = ['all']


