# Graphene
from graphene import ObjectType
from graphene import String
from graphene import Field
from graphene import List
from graphene import Int

# Django
from django.db.models import Q

# App
from .types import TrackType
from .models import Track

class Query(ObjectType):
    tracks         = List(TrackType, search=String())
    tracks_deleted = List(TrackType)
    track          = Field(TrackType, id = Int(required = True))

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

    def resolve_tracks_deleted(self, info):
        return Track.objects.all().filter(status = False)

    def resolve_track(self, info, id):
        track = Track.objects.get(id = id)
        return Query(track = track)
