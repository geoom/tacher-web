from django.conf.urls import patterns, include, url

from .views import TeacherListView, TeacherDetailView
from .api.v1 import urls as v1_urls

urlpatterns = patterns('apps.people.views',
    url(r'^teachers/$', TeacherListView.as_view(), name='teacher_list'),
    url(r'^teachers/(?P<pk>\d+)/$', TeacherDetailView.as_view(), name='teacher_detail'),

    # API config
    url(r'^api/', include(v1_urls)),
)