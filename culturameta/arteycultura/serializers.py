from rest_framework import serializers
from .models import Artista, Obra, Area, Biblioteca, Festival

class ArtistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artista
        fields = ['all']

class ObraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Obra
        fields = ['all']

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ['all']

class BibliotecaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Biblioteca
        fields = ['all']

class FestivalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Festival
        fields = ['all']