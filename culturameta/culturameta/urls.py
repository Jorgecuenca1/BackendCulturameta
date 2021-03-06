"""culturameta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from tutorials.urls import router
from arteycultura.urls import routera
from document.urls import routerd
from information.urls import routeri
from information import views as information_views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^admin/dynamic_raw_id/', include('dynamic_raw_id.urls')),

    path('api/', include((router.urls, 'restaurant'), namespace='restaurant')),
    path('api/', include((routera.urls, 'arteycultura'), namespace='arteycultura')),
    path('api/', include((routerd.urls, 'document'), namespace='document')),
    path('api/', include((routeri.urls, 'information'), namespace='information')),
    path('pqrsd/',information_views.pqrsd,name='pqrsd'),
    path('torneo/', information_views.torneo, name='torneo'),
    path('encuestatransparencia/', information_views.encuestatransparencia, name='pqrsd'),

]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
