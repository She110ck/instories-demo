from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django_redis import get_redis_connection

# Create your views here.
from notify.forms import PushForm
from notify.models import Push


def index(request):
    args = {}
    pushes = Push.objects.all()
    args = {'pushes': pushes}
    args = {'push_form':PushForm}
    args['gross'] = Push.objects.count()
    return render(request, 'notify/base.html', args)


def notify(request):
    get_redis_connection("default").flushall()
    return render(request, 'notify/notify.html', {})
