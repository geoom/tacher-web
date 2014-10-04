
from rest_framework import viewsets

from ...models import Teacher
from .resources import TeacherSerializer


class TeacherViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer