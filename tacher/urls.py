from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^$', 'tacher.views.home', name='home'),
    url(r'^about$', 'tacher.views.about', name='about'),

    url(r'^', include('apps.people.urls', namespace='people')),
    url(r'^', include('apps.ranking.urls', namespace='ranking')),
    url(r'^', include('apps.auth.urls', namespace='auth')),

    # Url for authentication
    url('', include('social.apps.django_app.urls', namespace='social')),

    url(r'^admin/', include(admin.site.urls)),
)
