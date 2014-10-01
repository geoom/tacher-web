
from django.http import HttpResponse
from django.shortcuts import render, redirect


def home(request):
    if not request.user.is_anonymous():
        template_name = "news-feed.html"
        context = {
            'user': request.user,
        }
    else:
        template_name = "home.html"
        context = {
            'msg': 'ola, esto es Tacher ... la venganza !!'
        }

    return render(request, template_name, context)


def about(request):
    return HttpResponse('This is a project to kill troll teachers ... muajajaja')
