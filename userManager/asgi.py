"""
ASGI config for userManager project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
# https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
# """

# import os

# from django.core.asgi import get_asgi_application
# from channels.routing import ProtocolTypeRouter, URLRouter
# from user import routing
# from channels.auth import AuthMiddlewareStack
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'userManager.settings')
# django_asgi_app = get_asgi_application()


# application = ProtocolTypeRouter({
#     "http": django_asgi_app,
#     "websocket": AuthMiddlewareStack(
#         URLRouter(
#             routing.websocket_urlpatterns
#         )
#     ),
# })
    
