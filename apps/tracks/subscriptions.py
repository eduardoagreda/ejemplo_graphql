import graphene

from graphene_subscriptions.events import CREATED

from .types import TrackType
from .models import Track

class TrackSubscription(graphene.ObjectType):
    track_created = graphene.Field(TrackType)

    def resolve_track_created(root, info):
        return root.filter(
            lambda event:
                event.operation == CREATED and
                isinstance(event.instance, Track)
        ).map(lambda event: event.instance)