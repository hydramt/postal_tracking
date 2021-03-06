"""postal_tracking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.shortcuts import render

urlpatterns = [
    path('alla/', admin.site.urls),
    path('', views.index),
    path('add', views.add),
    url(r'^del/(?P<id_del>[0-9]+)/$', views.delete),
    path('login', views.loginP, name='login_page'),
#    path('loginP', views.loginP),
    path('register', views.registerF),
    path('registerP/', views.registerP),
]
