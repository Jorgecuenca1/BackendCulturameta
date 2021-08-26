
from django.shortcuts import render
from rest_framework import viewsets


from .models import Employed, Sede, Objectives, MiVi, Functions, Coro, Information
from .serializers import EmployedSerializer, SedeSerializer, ObjectivesSerializer, MiViSerializer, FunctionsSerializer, \
    CoroSerializer, InformationSerializer
from rest_framework.response import Response
from culturameta.settings import HEADER_TOKEN

class EmployedViewSet(viewsets.ModelViewSet):

    def create(self, request, *args, **kwargs):
        request_token = request.headers.get('X-Custom-Header', None)
        if request_token is None or request_token != HEADER_TOKEN:
            return Response(status=400)
        return super(EmployedViewSet, self).create(request, *args, **kwargs)

    serializer_class = EmployedSerializer
    def get_queryset(self):
        return Employed.objects.all()

class SedeViewSet(viewsets.ModelViewSet):

    def create(self, request, *args, **kwargs):
        request_token = request.headers.get('X-Custom-Header', None)
        if request_token is None or request_token != HEADER_TOKEN:
            return Response(status=400)
        return super(SedeViewSet, self).create(request, *args, **kwargs)

    serializer_class = SedeSerializer
    def get_queryset(self):
        return Sede.objects.all()


class InformationViewSet(viewsets.ModelViewSet):

    def create(self, request, *args, **kwargs):
        request_token = request.headers.get('X-Custom-Header', None)
        if request_token is None or request_token != HEADER_TOKEN:
            return Response(status=400)
        return super(InformationViewSet, self).create(request, *args, **kwargs)

    serializer_class = InformationSerializer

    def get_queryset(self):
        return Information.objects.all()

class ObjectivesViewSet(viewsets.ModelViewSet):

    def create(self, request, *args, **kwargs):
        request_token = request.headers.get('X-Custom-Header', None)
        if request_token is None or request_token != HEADER_TOKEN:
            return Response(status=400)
        return super(ObjectivesViewSet, self).create(request, *args, **kwargs)

    serializer_class = ObjectivesSerializer
    def get_queryset(self):
        return Objectives.objects.all()


class MiViViewSet(viewsets.ModelViewSet):
    def create(self, request, *args, **kwargs):
        request_token = request.headers.get('X-Custom-Header', None)
        if request_token is None or request_token != HEADER_TOKEN:
            return Response(status=400)
        return super(MiViViewSet, self).create(request, *args, **kwargs)

    serializer_class = MiViSerializer
    def get_queryset(self):
        return MiVi.objects.all()

class FunctionsViewSet(viewsets.ModelViewSet):

    def create(self, request, *args, **kwargs):
        request_token = request.headers.get('X-Custom-Header', None)
        if request_token is None or request_token != HEADER_TOKEN:
            return Response(status=400)
        return super(FunctionsViewSet, self).create(request, *args, **kwargs)

    serializer_class = FunctionsSerializer
    def get_queryset(self):
        return Functions.objects.all()

class CoroViewSet(viewsets.ModelViewSet):

    def create(self, request, *args, **kwargs):
        request_token = request.headers.get('X-Custom-Header', None)
        if request_token is None or request_token != HEADER_TOKEN:
            return Response(status=400)
        return super(CoroViewSet, self).create(request, *args, **kwargs)


    serializer_class = CoroSerializer
    def get_queryset(self):
        return Coro.objects.all()