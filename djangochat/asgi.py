import os
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

django_asgi_app = get_asgi_application()

from room.routing import *


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangochat.settings')
application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    )
})
