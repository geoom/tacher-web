
from django.http import HttpResponse
from django.shortcuts import render

from .models import Teacher

from django.core import serializers


def teacher_list(request):
    template_name = "teacher-list.html"

    teachers = Teacher.objects.all()

    return render(request, template_name, {'teachers': teachers})


def get_json(request):
    data = serializers.serialize("json", Teacher.objects.all())
    return HttpResponse(data, mimetype='application/json')
