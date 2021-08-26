from django.shortcuts import render
from rest_framework import viewsets
from .models import Artista, Obra, Area, Biblioteca, Festival, Noticia
from .serializers import ArtistaSerializer, ObraSerializer, AreaSerializer, BibliotecaSerializer, FestivalSerializer, \
    NoticiaSerializer
from rest_framework.response import Response
from culturameta.settings import HEADER_TOKEN

class ArtistaViewSet(viewsets.ModelViewSet):
    def create(self, request, *args, **kwargs):
        request_token = request.headers.get('X-Custom-Header', None)
        if request_token is None or request_token != HEADER_TOKEN:
            return Response(status=400)
        return super(ArtistaViewSet, self).create(request, *args, **kwargs)

    serializer_class = ArtistaSerializer

    def get_queryset(self):
        return Artista.objects.all()

class ObraViewSet(viewsets.ModelViewSet):
    def create(self, request, *args, **kwargs):
        request_token = request.headers.get('X-Custom-Header', None)
        if request_token is None or request_token != HEADER_TOKEN:
            return Response(status=400)
        return super(ObraViewSet, self).create(request, *args, **kwargs)


    serializer_class = ObraSerializer

    def get_queryset(self):
        return Obra.objects.all()

class AreaViewSet(viewsets.ModelViewSet):
    def create(self, request, *args, **kwargs):
        request_token = request.headers.get('X-Custom-Header', None)
        if request_token is None or request_token != HEADER_TOKEN:
            return Response(status=400)
        return super(AreaViewSet, self).create(request, *args, **kwargs)


    serializer_class = AreaSerializer

    def get_queryset(self):
        return Area.objects.all()

class BibliotecaViewSet(viewsets.ModelViewSet):

    def create(self, request, *args, **kwargs):
        request_token = request.headers.get('X-Custom-Header', None)
        if request_token is None or request_token != HEADER_TOKEN:
            return Response(status=400)
        return super(BibliotecaViewSet, self).create(request, *args, **kwargs)

    serializer_class = BibliotecaSerializer

    def get_queryset(self):
        return Biblioteca.objects.all()

class FestivalViewSet(viewsets.ModelViewSet):

    def create(self, request, *args, **kwargs):
        request_token = request.headers.get('X-Custom-Header', None)
        if request_token is None or request_token != HEADER_TOKEN:
            return Response(status=400)
        return super(FestivalViewSet, self).create(request, *args, **kwargs)

    serializer_class = FestivalSerializer

    def get_queryset(self):
        return Festival.objects.all()

class NoticiaViewSet(viewsets.ModelViewSet):

    def create(self, request, *args, **kwargs):
        request_token = request.headers.get('X-Custom-Header', None)
        if request_token is None or request_token != HEADER_TOKEN:
            return Response(status=400)
        return super(NoticiaViewSet, self).create(request, *args, **kwargs)

    serializer_class = NoticiaSerializer

    def get_queryset(self):
        if self.request.method == 'GET':
            queryset = Noticia.objects.all()
            orden = self.request.GET.get('orden', None)
            if orden is not None:
                queryset = queryset.filter(orden=orden)
                return queryset
