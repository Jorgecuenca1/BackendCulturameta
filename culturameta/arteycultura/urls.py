from rest_framework import routers
from .views import ArtistaViewSet, ObraViewSet, AreaViewSet, BibliotecaViewSet, FestivalViewSet, NoticiaViewSet

routera = routers.SimpleRouter()
routera.register(r'artista', ArtistaViewSet, basename='artista'),
routera.register(r'obra', ObraViewSet, basename='obra'),
routera.register(r'area', AreaViewSet, basename='area'),
routera.register(r'biblioteca', ObraViewSet, basename='obra'),
routera.register(r'festival', AreaViewSet, basename='area'),
routera.register(r'noticia', NoticiaViewSet, basename='noticia'),