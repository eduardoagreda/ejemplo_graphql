from graphene_django import DjangoObjectType

from .models import Track

class TrackType(DjangoObjectType):
    class Meta:
        model = Track
