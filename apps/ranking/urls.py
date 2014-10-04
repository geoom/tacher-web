from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'ranking/$', 'apps.ranking.views.ranking', name='ranking'),
)
