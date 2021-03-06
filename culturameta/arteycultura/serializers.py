from rest_framework import serializers
from .models import Artista, Obra, Area, Biblioteca, Festival, Noticia


class ArtistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artista
        fields = ['name','last_name','age','cedula','lugar_nacimiento']

class ObraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Obra
        fields = ['name','name_obra','artista','ubicacion','description','image',]

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ['name','information', 'tittle1', 'description1', 'tittle2', 'description2','icono','history']

class BibliotecaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Biblioteca
        fields = ['name','libro', 'librarian', 'adress', 'zone', 'resolution', 'description', 'history', 'orden']

class FestivalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Festival
        fields = ['name','description','orden','fecha']

class NoticiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Noticia
        fields = ['name','descripcion','orden','file']