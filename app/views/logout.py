from django.contrib.auth import logout
from django.shortcuts import redirect


def logout_page(request):
    logout(request)
    return redirect('index')
