from rest_framework import serializers
from .models import Image, Module, SubModule, Document

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['all']

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ['all']
class SubModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubModule
        fields = ['all']

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['all']

