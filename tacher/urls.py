from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^$', 'tacher.views.home', name='home'),
    url(r'^about$', 'tacher.views.about', name='about'),

    url(r'^', include('apps.people.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^', include('apps.ranking.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
