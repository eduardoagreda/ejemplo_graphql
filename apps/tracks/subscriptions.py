import graphene

from graphene_subscriptions.events import CREATED

from .types import TrackType, LikeType
from .models import Track, Like


class TrackSubscription(graphene.ObjectType):
    track_created = graphene.Field(TrackType)

    def resolve_track_created(root, info):
        return root.filter(
            lambda event:
                event.operation == CREATED and
                isinstance(event.instance, Track)
        ).map(lambda event: event.instance)

class LikeSubscription(graphene.ObjectType):
    like_created = graphene.Field(LikeType)

    def resolve_like_created(root, info):
        return root.filter(
            lambda event:
                event.operation == CREATED and
                isinstance(event.instance, Like)
        ).map(lambda event: event.instance)
