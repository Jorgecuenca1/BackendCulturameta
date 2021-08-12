from django.shortcuts import render
from rest_framework import viewsets
from .models import Artista, Obra, Area, Biblioteca, Festival, Noticia
from .serializers import ArtistaSerializer, ObraSerializer, AreaSerializer, BibliotecaSerializer, FestivalSerializer, \
    NoticiaSerializer


class ArtistaViewSet(viewsets.ModelViewSet):
    serializer_class = ArtistaSerializer

    def get_queryset(self):
        return Artista.objects.all()

class ObraViewSet(viewsets.ModelViewSet):
    serializer_class = ObraSerializer

    def get_queryset(self):
        return Obra.objects.all()

class AreaViewSet(viewsets.ModelViewSet):
    serializer_class = AreaSerializer

    def get_queryset(self):
        return Area.objects.all()

class BibliotecaViewSet(viewsets.ModelViewSet):
    serializer_class = BibliotecaSerializer

    def get_queryset(self):
        return Biblioteca.objects.all()

class FestivalViewSet(viewsets.ModelViewSet):
    serializer_class = FestivalSerializer

    def get_queryset(self):
        return Festival.objects.all()

class NoticiaViewSet(viewsets.ModelViewSet):
    serializer_class = NoticiaSerializer

    def get_queryset(self):
        if self.request.method == 'GET':
            queryset = Noticia.objects.all()
            orden = self.request.GET.get('orden', None)
            if orden is not None:
                queryset = queryset.filter(orden=orden)
                return queryset
