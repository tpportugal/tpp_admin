import graphene
from graphene_django.debug import DjangoDebug

from api.apps.geographical.counties import schema as CountySchema
from api.apps.geographical.districts import schema as DistrictSchema
from api.apps.geographical.places import schema as PlaceSchema
from api.apps.gtfs.agencies import schema as AgencySchema
from api.apps.gtfs.calendardates import schema as CalendarDateSchema
from api.apps.gtfs.routes import schema as RouteSchema
from api.apps.gtfs.services import schema as ServiceSchema
from api.apps.gtfs.stops import schema as StopSchema
from api.apps.gtfs.trips import schema as TripSchema


class Query(DistrictSchema.Query,
            CountySchema.Query,
            PlaceSchema.Query,
            AgencySchema.Query,
            CalendarDateSchema.Query,
            RouteSchema.Query,
            ServiceSchema.Query,
            StopSchema.Query,
            TripSchema.Query,
            graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
