from rest_framework import serializers
from .models import Image, Module, SubModule, Document, Accountability


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['name','imagen',]

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ['name',]

class SubModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubModule
        fields = ['name','module',]

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['name','name_archive','age','month','description','orden','module','submodule','url',]

class AccountabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Accountability
        fields = ['accountability','url','file']

