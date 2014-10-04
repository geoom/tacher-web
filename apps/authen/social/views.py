from django.contrib.auth import login
from django.http import HttpResponse, HttpResponseBadRequest

from social.apps.django_app.utils import load_strategy, load_backend

def signin_by_access_token(request, backend):

    auth_token = request.GET.get('access_token')
    backend = load_backend(load_strategy(request=request), backend, None)

    try:
        user = backend.do_auth(auth_token)
    except Exception:
        return HttpResponse('ERROR')

    if user:
        login(request, user)
        return HttpResponse('OK')
    return HttpResponse('ERROR')