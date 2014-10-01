from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect

@login_required()
def signout(request):
    logout(request)
    return redirect('/')
