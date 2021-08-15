from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include
from tutorials.urls import router
from arteycultura.urls import routera
from document.urls import routerd
from information.urls import routeri
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^admin/dynamic_raw_id/', include('dynamic_raw_id.urls')),

    path('api/', include((router.urls, 'restaurant'), namespace='restaurant')),
    path('api/', include((routera.urls, 'arteycultura'), namespace='arteycultura')),
    path('api/', include((routerd.urls, 'document'), namespace='document')),
    path('api/', include((routeri.urls, 'information'), namespace='information')),

]

if settings.DEBUG:
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns += [
            path("__debug__/", include(debug_toolbar.urls))
        ]

    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
