from rest_framework import serializers
from .models import Employed, Sede

class EmployedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employed
        fields = ['name','contact','carge','extension','phone','fax','email',]

class SedeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sede
        fields = ['name','type','adress','city','phone','fax','email',]


