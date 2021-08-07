from rest_framework import routers
from .views import ImageViewSet, ModuleViewSet, SubModuleViewSet, DocumentViewSet, AccountabilityViewSet

routerd = routers.SimpleRouter()
routerd.register(r'image', ImageViewSet, basename='image'),
routerd.register(r'module', ModuleViewSet, basename='module'),
routerd.register(r'submodule', SubModuleViewSet, basename='submodule'),
routerd.register(r'document', DocumentViewSet, basename='document'),
routerd.register(r'accountability', AccountabilityViewSet, basename='accountability'),