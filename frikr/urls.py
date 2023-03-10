"""frikr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from photos import views
from users import views as user_view

from photos.views import HomeView, DetailView, CreateView
from users.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Photos URLS
    path('', HomeView.as_view(), name='photos_home'),
    path('photo/<pk>', DetailView.as_view(), name='photo_detail'),
    path('photos/new', CreateView.as_view(), name='create_photo'),


    # Users URLS
    path('login', LoginView.as_view(), name='users_login'),
    path('logout', LogoutView.as_view(), name='users_logout')
]
