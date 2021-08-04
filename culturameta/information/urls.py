from rest_framework import routers
from .views import EmployedViewSet, SedeViewSet
routeri = routers.SimpleRouter()
routeri.register(r'employed', EmployedViewSet, basename='employed'),
routeri.register(r'sede', SedeViewSet, basename='sede'),