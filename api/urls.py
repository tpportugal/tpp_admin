from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import include
from django.views.generic import RedirectView
from graphene_django.views import GraphQLView
from api.apps.gdrive.views import upload_timetable


urlpatterns = [
    #url(r'^$', RedirectView.as_view(url='/mvp', permanent=False)),
    url(r'^api/', GraphQLView.as_view(graphiql=getattr(settings, "GRAPHQL_EDITOR", False))),
    url(r'^$', admin.site.urls),
    url(r'^upload/', upload_timetable),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
