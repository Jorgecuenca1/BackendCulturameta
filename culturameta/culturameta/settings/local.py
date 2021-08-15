from .base import *

DEBUG = True

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS += ['debug_toolbar', 'drf_yasg',]

MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]

DEBUG_TOOLBAR_CONFIG = {
    "DISABLE_PANELS": ["debug_toolbar.panels.redirects.RedirectsPanel"],
    'SHOW_TOOLBAR_CALLBACK': lambda request: DEBUG
}


SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'basic': {
            'type': 'basic'
        }
    },
}