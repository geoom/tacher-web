from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', 'tacher_web.views.home', name='home'),
    url(r'^about$', 'tacher_web.views.about', name='about'),

    url(r'^', include('apps.people.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^', include('apps.ranking.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
