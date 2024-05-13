import os
import django
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangochat.settings')
django_asgi_app = get_asgi_application()


from room.routing import *


application = ProtocolTypeRouter({
  "https": django_asgi_app,
  "websocket": AuthMiddlewareStack(
    URLRouter(
        websocket_urlpatterns
    )
 ),
 })
