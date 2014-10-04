from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^/signout/$', 'apps.auth.views.signout', name='signout'),
)

