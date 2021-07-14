from graphene import ObjectType
from graphene import Schema

# Queries
from apps.tracks.schema import Query as TrackQuery

# Mutations
from apps.tracks.mutations import Mutation as TrackMutations

# Subscriptions
from apps.tracks.subscriptions import TrackSubscription

class Query(TrackQuery, ObjectType):
    pass

class Mutation(TrackMutations, ObjectType):
    pass

class Subscription(TrackSubscription):
    pass


schema = Schema(query=Query, mutation=Mutation, subscription=Subscription, auto_camelcase=False)
