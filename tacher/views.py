
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    template_name = "home.html"
    return render(request, template_name, {'msg': 'ola, esto es Tacher ... la venganza !!'})


def about(request):
    return HttpResponse('This is a project to kill troll teachers ... muajajaja')

def dashboard(request):
    template_name = "newsfeed.html"
    return render(request, template_name, {})


def ranking(request):
    template_name = "ranking.html"
    return render(request, template_name, {})