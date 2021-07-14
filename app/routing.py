# Django
from django.urls import path 

# Channels
from channels.routing import ProtocolTypeRouter, URLRouter

# Graphene Subscriptions
from graphene_subscriptions.consumers import GraphqlSubscriptionConsumer

application = ProtocolTypeRouter({
    "websocket": URLRouter([
        path('graphql-ws/', GraphqlSubscriptionConsumer)
    ]),
})