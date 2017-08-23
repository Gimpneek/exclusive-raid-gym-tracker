from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render


def login_page(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user=user)
            return redirect('gym_list')
        else:
            return redirect('login')
    else:
        return render(request, 'app/login.html')