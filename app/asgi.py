"""
ASGI config for app project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/asgi/
"""
import os

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from django.urls import path 

from graphene_subscriptions.consumers import GraphqlSubscriptionConsumer


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

application = ProtocolTypeRouter({
    "ws": get_asgi_application(),
    "websocket": URLRouter([
        path('graphql-ws/', GraphqlSubscriptionConsumer)
    ]),
})
