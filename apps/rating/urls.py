
from django.conf.urls import patterns, include, url

from .api.v1 import urls as v1_urls

urlpatterns = patterns('',
    # url(r'rating/$', 'apps.rating.views.rating', name='rating'),

    # API config
    url(r'^api/', include(v1_urls)),
)
