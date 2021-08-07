from rest_framework import routers
from .views import EmployedViewSet, SedeViewSet, InformationViewSet, ObjectivesViewSet, MiViViewSet, FunctionsViewSet, \
    CoroViewSet

routeri = routers.SimpleRouter()
routeri.register(r'employed', EmployedViewSet, basename='employed'),
routeri.register(r'sede', SedeViewSet, basename='sede'),
routeri.register(r'information', InformationViewSet, basename='information'),
routeri.register(r'objectives', ObjectivesViewSet, basename='objectives'),
routeri.register(r'mivi', MiViViewSet, basename='mivi'),
routeri.register(r'functions', FunctionsViewSet, basename='functions'),
routeri.register(r'coro', CoroViewSet, basename='coro'),