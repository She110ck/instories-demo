from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/notify')
        else:
            messages.error(request, 'username or password not correct')
            return redirect('login')

    return render(request, 'notify/login.html', {})


def custom_logout(request):
    logout(request)
    return redirect('/login')
