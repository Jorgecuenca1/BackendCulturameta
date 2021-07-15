from rest_framework import routers
from .views import MenuViewSet
router = routers.SimpleRouter()
router.register(r'menu', MenuViewSet, basename='menu')