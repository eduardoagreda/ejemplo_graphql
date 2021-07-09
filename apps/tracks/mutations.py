import graphene

from .types import TrackType
from .models import Track

class CreateTrack(graphene.Mutation):
    track = graphene.Field(TrackType)

    class Arguments:
        title       = graphene.String()
        description = graphene.String()
        url         = graphene.String()

    def mutate(self, info, title, description, url):
        track = Track(title=title, description=description,
                      url=url)
        track.save()
        return CreateTrack(track=track)

class UpdateTrack(graphene.Mutation):
    track = graphene.Field(TrackType)

    class Arguments:
        track_id    = graphene.Int(required=True)
        title       = graphene.String()
        description = graphene.String()
        url         = graphene.String()

    def mutate(self, info, track_id, title, url, description):
        track = Track.objects.get(id=track_id)

        track.title       = title
        track.description = description
        track.url         = url

        track.save()

        return UpdateTrack(track=track)

class DeleteTrack(graphene.Mutation):
    track_id = graphene.Int()

    class Arguments:
        track_id = graphene.Int(required=True)

    def mutate(self, info, track_id):
        track = Track.objects.get(id=track_id)

        track.delete()

        return DeleteTrack(track_id=track_id)

class Mutation(graphene.ObjectType):
    create_track = CreateTrack.Field()
    update_track = UpdateTrack.Field()
    delete_track = DeleteTrack.Field()