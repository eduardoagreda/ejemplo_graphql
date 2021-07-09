import graphene
import graphql_jwt

# Queries
from apps.tracks.schema import Query as TrackQuery
from apps.users.schema import Query as UserQuery

# Mutations
from apps.tracks.mutations import Mutation as TrackMutations
from apps.users.mutations import Mutation as UserMutations

# Subscriptions
from apps.tracks.subscriptions import TrackSubscription, LikeSubscription
from apps.users.subscriptions import UserSubscription


class Query(UserQuery, TrackQuery, graphene.ObjectType):
    pass


class Mutation(UserMutations, TrackMutations, graphene.ObjectType):
    token_auth    = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token  = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

class Subscription(TrackSubscription, LikeSubscription):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation, subscription=Subscription)
