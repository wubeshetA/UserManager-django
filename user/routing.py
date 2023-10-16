# routing.py

from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from .consumers import UserConsumer
from django.urls import re_path


websocket_urlpatterns = [
    re_path(r'ws/users/$', UserConsumer.as_asgi()),
]