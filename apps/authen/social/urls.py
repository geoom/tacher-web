from django.conf.urls import patterns, url
from .views import signin_by_access_token

urlpatterns = patterns('',
    url(r'^signin-by-token/(?P<backend>[^/]+)/$', signin_by_access_token),
)
