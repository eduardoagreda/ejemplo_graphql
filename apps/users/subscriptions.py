import graphene

from graphene_subscriptions.events import CREATED

from .types import UserType

from django.contrib.auth import get_user_model

class UserSubscription(graphene.ObjectType):
    user_created = graphene.Field(UserType)

    def resolve_user_created(root, info):
        return root.filter(
            lambda event:
                event.operation == CREATED and
                isinstance(event.instance, get_user_model())
        ).map(lambda event: event.instance)
