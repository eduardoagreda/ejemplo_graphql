import graphene

from django.db.models import Q

from .types import TrackType, LikeType
from .models import Track, Like


class Query(graphene.ObjectType):
    tracks = graphene.List(TrackType, search=graphene.String())
    likes = graphene.List(LikeType)

    def resolve_tracks(self, info, search=None):
        if search:
            filter = (
                Q(title__icontains=search) |
                Q(description__icontains=search) |
                Q(url__icontains=search) |
                Q(posted_by__username__icontains=search)
            )
            return Track.objects.filter(filter)

        return Track.objects.all()

    def resolve_likes(self, info):
        return Like.objects.all()
