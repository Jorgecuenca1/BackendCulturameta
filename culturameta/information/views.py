
from django.shortcuts import render
from rest_framework import viewsets
from django.shortcuts import render, redirect
from .forms import TorneoForm, PqrsdForm, EncuestaTransparenciaForm
from .models import Employed, Sede, Objectives, MiVi, Functions, Coro, Information, Patrimonio
from .serializers import EmployedSerializer, PatrimonioSerializer,SedeSerializer, ObjectivesSerializer, MiViSerializer, FunctionsSerializer, \
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
        if self.request.method == 'GET':
            queryset = Employed.objects.all()
            phone = self.request.GET.get('phone', None)
            if phone is not None:
                queryset = queryset.filter(phone=phone)
                return queryset






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


class PatrimonioViewSet(viewsets.ModelViewSet):

    def create(self, request, *args, **kwargs):
        request_token = request.headers.get('X-Custom-Header', None)
        if request_token is None or request_token != HEADER_TOKEN:
            return Response(status=400)
        return super(PatrimonioViewSet, self).create(request, *args, **kwargs)


    serializer_class = PatrimonioSerializer
    def get_queryset(self):
        return Patrimonio.objects.all()


class CoroViewSet(viewsets.ModelViewSet):

    def create(self, request, *args, **kwargs):
        request_token = request.headers.get('X-Custom-Header', None)
        if request_token is None or request_token != HEADER_TOKEN:
            return Response(status=400)
        return super(CoroViewSet, self).create(request, *args, **kwargs)


    serializer_class = CoroSerializer
    def get_queryset(self):
        return Coro.objects.all()

def torneo(request):
    if request.method == "POST":
        # update DB
        form = TorneoForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('https://culturameta.gov.co')
    else:
        # show the form
        form = TorneoForm()

    context = {'form': form}
    return render(request, 'torneo.html', context)

def pqrsd(request):
    if request.method == "POST":
        # update DB
        form = PqrsdForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('https://culturameta.gov.co')
    else:
        # show the form
        form = PqrsdForm()

    context = {'form': form}
    return render(request, 'pqrsd.html', context)

def encuestatransparencia(request):
    if request.method == "POST":
        # update DB
        form = EncuestaTransparenciaForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('https://culturameta.gov.co')
    else:
        # show the form
        form = EncuestaTransparenciaForm()

    context = {'form': form}
    return render(request, 'encuestatransparencia.html', context)