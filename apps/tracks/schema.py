import graphene

from django.db.models import Q

from .types import TrackType
from .models import Track

class Query(graphene.ObjectType):
    tracks = graphene.List(TrackType, search=graphene.String())

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
