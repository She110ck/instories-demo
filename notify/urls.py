
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('notify/send/', views.notify_send, name='notify'),
]
