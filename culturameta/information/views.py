
from django.shortcuts import render
from rest_framework import viewsets
from .models import Employed, Sede, Objectives, MiVi, Functions, Coro, Information
from .serializers import EmployedSerializer, SedeSerializer, ObjectivesSerializer, MiViSerializer, FunctionsSerializer, \
    CoroSerializer, InformationSerializer


class EmployedViewSet(viewsets.ModelViewSet):
    serializer_class = EmployedSerializer
    def get_queryset(self):
        return Employed.objects.all()

class SedeViewSet(viewsets.ModelViewSet):
    serializer_class = SedeSerializer
    def get_queryset(self):
        return Sede.objects.all()


class InformationViewSet(viewsets.ModelViewSet):
    serializer_class = InformationSerializer

    def get_queryset(self):
        return Information.objects.all()

class ObjectivesViewSet(viewsets.ModelViewSet):
    serializer_class = ObjectivesSerializer
    def get_queryset(self):
        return Objectives.objects.all()


class MiViViewSet(viewsets.ModelViewSet):
    serializer_class = MiViSerializer
    def get_queryset(self):
        return MiVi.objects.all()

class FunctionsViewSet(viewsets.ModelViewSet):
    serializer_class = FunctionsSerializer
    def get_queryset(self):
        return Functions.objects.all()

class CoroViewSet(viewsets.ModelViewSet):
    serializer_class = CoroSerializer
    def get_queryset(self):
        return Coro.objects.all()