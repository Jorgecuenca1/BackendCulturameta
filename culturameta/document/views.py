
from django.shortcuts import render
from rest_framework import viewsets
from .models import Image, Module, SubModule, Document, Accountability
from .serializers import ImageSerializer, ModuleSerializer, SubModuleSerializer, DocumentSerializer, \
    AccountabilitySerializer


class ImageViewSet(viewsets.ModelViewSet):
    serializer_class = ImageSerializer
    def get_queryset(self):
        return Image.objects.all()

class ModuleViewSet(viewsets.ModelViewSet):
    serializer_class = ModuleSerializer
    def get_queryset(self):
        return Module.objects.all()

class SubModuleViewSet(viewsets.ModelViewSet):
    serializer_class = SubModuleSerializer
    def get_queryset(self):
        return SubModule.objects.all()

class DocumentViewSet(viewsets.ModelViewSet):
    serializer_class = DocumentSerializer
    def get_queryset(self):
        return Document.objects.all()

class AccountabilityViewSet(viewsets.ModelViewSet):
    serializer_class = AccountabilitySerializer
    def get_queryset(self):
        return Accountability.objects.all()