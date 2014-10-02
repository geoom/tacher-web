from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^/signout$', 'apps.authen.views.signout', name='signout'),

	url(r'^social/', include('apps.authen.social.urls')),
)

