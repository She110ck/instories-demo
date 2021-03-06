"""instories URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from cruds_adminlte.urls import crud_for_app
from cruds_adminlte.urls import crud_for_model

from django.apps import apps

from instories import views

urlpatterns = [
    path('accounts/login/', views.custom_login, name='login'),
    path('logout/', views.custom_logout, name='logout'),
    # path('notify/', include('notify.urls')),
    path('', include('notify.urls')),
    path('admin/', admin.site.urls),
]
urlpatterns += crud_for_app('notify', login_required=True,
                            check_perms=True)

# urlpatterns += crud_for_model(apps.get_model('notify', 'Option'))
# urlpatterns += crud_for_model(apps.get_model('notify', 'Push'))
