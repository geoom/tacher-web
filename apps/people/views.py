
from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from braces.views import LoginRequiredMixin

from .models import Teacher
from django.core import serializers


class TeacherListView(LoginRequiredMixin, ListView):

    model = Teacher
    queryset = Teacher.objects.all()


class TeacherDetailView(LoginRequiredMixin, DetailView):

    model = Teacher


def get_json(request):
    data = serializers.serialize("json", Teacher.objects.all())
    return HttpResponse(data, mimetype='application/json')
