
from django.http import HttpResponse
from django.shortcuts import render, redirect

from apps.people.models import Teacher


def home(request):
    if not request.user.is_anonymous():
        template_name = "news_feed.html"
        context = {
            'user': request.user,
            'teachers': Teacher.objects.all(),
        }
    else:
        template_name = "home.html"
        context = {
            'msg': 'ola, esto es Tacher ... la venganza !!'
        }

    return render(request, template_name, context)


def about(request):
    return HttpResponse('This is a project to kill troll teachers ... muajajaja')
