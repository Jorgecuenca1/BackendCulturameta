
from django.shortcuts import render
from rest_framework import viewsets
from .models import Employed, Sede
from .serializers import EmployedSerializer, SedeSerializer

class EmployedViewSet(viewsets.ModelViewSet):
    serializer_class = EmployedSerializer
    def get_queryset(self):
        return Employed.objects.all()

class SedeViewSet(viewsets.ModelViewSet):
    serializer_class = SedeSerializer
    def get_queryset(self):
        return Sede.objects.all()