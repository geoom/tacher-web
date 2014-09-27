
from django.http import HttpResponse
from django.shortcuts import render
from apps.ranking.models import Record

def ranking(request):
    template_name = "ranking.html"
    ranking = Record.objects.all()

    return render(request, template_name, {'ranking': ranking})
