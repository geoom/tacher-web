
from django.http import HttpResponse
from django.shortcuts import render

def ranking(request):
    template_name = "rating.html"

    return HttpResponse('ranking')
