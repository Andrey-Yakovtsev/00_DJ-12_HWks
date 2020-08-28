"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.http import HttpResponseRedirect
from django.urls import path
from .views import table_view, current_time_view, workdir_view, home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('table/', table_view, name='table'),
    path('current_time/', current_time_view, name='time'),
    path('workdir/', workdir_view, name='workdir'),
    path('index/', home_view, name='home'),
    path('', lambda x: HttpResponseRedirect('/index/')),
]
