# -*- coding: utf-8 -*
from django.conf.urls import patterns, include, url


from . import views

urlpatterns = patterns('',
    url(r'^options/$', views.RatingOptionList.as_view()),

    url(r'^docs/', include('rest_framework_swagger.urls', namespace='swagger'))
)

