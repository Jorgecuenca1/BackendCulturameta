
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
        if self.request.method == 'GET':
            queryset = Document.objects.all()
            age = self.request.GET.get('year', None)
            module = self.request.GET.get('module', None)
            submodule = self.request.GET.get('submodule',None)
            if module is not None:
                queryset = queryset.filter(module=module)
                return queryset
            if module and submodule is not None:
                queryset = queryset.filter(module=module, submodule=submodule)
                return queryset
            if age and submodule is not None:
                queryset = queryset.filter(age=age,submodule=submodule)
                return queryset
            if module and age is not None:
                queryset = queryset.filter(age=age, module=module)
                return queryset
            if module and age and submodule is not None:
                queryset = queryset.filter(age=age, module=module, submodule=submodule)
                return queryset




class AccountabilityViewSet(viewsets.ModelViewSet):
    serializer_class = AccountabilitySerializer
    def get_queryset(self):
        return Accountability.objects.all()