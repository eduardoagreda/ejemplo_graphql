import graphene

# Queries
from apps.tracks.schema import Query as TrackQuery

# Mutations
from apps.tracks.mutations import Mutation as TrackMutations

# Subscriptions
from apps.tracks.subscriptions import TrackSubscription

class Query(TrackQuery, graphene.ObjectType):
    pass

class Mutation(TrackMutations, graphene.ObjectType):
    pass

class Subscription(TrackSubscription):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation, subscription=Subscription)
