# menu/viewsets.py
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Menu
from .serializers import MenuSerializer
from ..culturameta.settings import HEADER_TOKEN


class MenuViewSet(viewsets.ModelViewSet):

    def create(self, request, *args, **kwargs):
        request_token = request.headers.get('X-Custom-Header', None)
        if request_token is None or request_token != HEADER_TOKEN:
            return Response(status=400)
        return super(MenuViewSet, self).create(request, *args, **kwargs)

    serializer_class = MenuSerializer

    def get_queryset(self):
        return Menu.objects.all()
