from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django_adminlte.compat import is_authenticated
from django_redis import get_redis_connection

# Create your views here.
from notify.forms import PushForm
from notify.models import Push


def index(request):
    if request.user.is_authenticated:
        args = {'push_form': PushForm()}
        return render(request, 'notify/base.html', args)
    else:
        messages.error(request, 'login required')
        return redirect('/accounts/login')


def notify_send(request):
    if request.method == 'POST':
        push = PushForm(request.POST)
        print("ERROR: ", push.errors)
        push.save(commit=True)
    # get_redis_connection("default").flushall()
    return redirect('/notify/push/list')
