from django.conf.urls import patterns, include, url

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'teachers', views.TeacherViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    
    url(r'^docs/', include('rest_framework_swagger.urls', namespace='swagger'))
)

