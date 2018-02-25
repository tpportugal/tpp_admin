import graphene
from graphene_django import DjangoObjectType

from .models import Stop


class StopType(DjangoObjectType):
    class Meta:
        model = Stop


class Query(object):
    stop = graphene.Field(StopType,
                          id=graphene.Int(),
                          name=graphene.String(),
                          latitude=graphene.Float(),
                          longitude=graphene.Float())

    stops = graphene.List(StopType)

    def resolve_stop(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')
        latitude = kwargs.get('latitude')
        longitude = kwargs.get('longitude')

        if id is not None:
            return Stop.objects.get(pk=id)

        if name is not None:
            return Stop.objects.get(name=name)

        if latitude is not None:
            return Stop.objects.get(latitude=latitude)

        if longitude is not None:
            return Stop.objects.get(longitude=longitude)

        return None

    def resolve_stops(self, info, **kwargs):
        return Stop.objects.all()
