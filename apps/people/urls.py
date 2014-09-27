from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^teachers$', 'apps.people.views.teacher_list', name='teacher_list.html'),
)

urlpatterns += patterns('',
    url(r'^api/teachers.json$', 'apps.people.views.get_json', name='api_teachers'),
)

