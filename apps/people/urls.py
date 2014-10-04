from django.conf.urls import patterns, url

from .views import TeacherListView, TeacherDetailView

urlpatterns = patterns('apps.people.views',
    url(r'^teachers/$', TeacherListView.as_view(), name='teacher_list'),
    url(r'^teachers/(?P<pk>\d+)/$', TeacherDetailView.as_view(), name='teacher_detail'),
)

urlpatterns += patterns('',
    url(r'^api/teachers.json$', 'apps.people.views.get_json', name='api_teachers'),
)

