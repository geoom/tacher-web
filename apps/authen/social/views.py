import json

from django.contrib.auth import login
from django.http import HttpResponse, HttpResponseBadRequest

from social.apps.django_app.utils import load_strategy, load_backend


def signin_by_access_token(request, backend):

    auth_token = request.GET.get('access_token')
    backend = load_backend(load_strategy(request=request), backend, None)
    response = {
        'status': False,
    }

    try:
        user = backend.do_auth(auth_token)

        if user:
            login(request, user)
            response.update({'status': True})
            response.update(dict(user={'id': user.id}))
            print "ok"
    except Exception as e:
        print "error"
        print e
        # pass

    return HttpResponse(json.dumps(response), content_type='application/json')