from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',

    url(r'^$', 'tacher.views.home', name='home'),
    url(r'^about$', 'tacher.views.about', name='about'),

    url(r'^', include('apps.people.urls', namespace='people')),
    url(r'^', include('apps.rating.urls', namespace='rating')),
    url(r'^', include('apps.authen.urls', namespace='authen')),

    # social auth config
    url(r'^social/', include('social.apps.django_app.urls', namespace='social')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

)

urlpatterns += patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, }),
)