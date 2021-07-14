# Graphene
from graphene import ObjectType
from graphene import Field

# Graphene Subscriptions
from graphene_subscriptions.events import CREATED

# App
from .types import TrackType
from .models import Track

class TrackSubscription(ObjectType):
    track_created = Field(TrackType)

    def resolve_track_created(root, info):
        message = root.filter(
            lambda event:
                event.operation == CREATED and
                isinstance(event.instance, Track)
        ).map(lambda event: event.instance)
        return message