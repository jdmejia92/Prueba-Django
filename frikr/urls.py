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
from django.contrib.auth.decorators import login_required

from photos.views import HomeView, DetailView, CreateView, PhotoListView, UserPhotosView
from photos.api import PhotoListAPI, PhotoDetailAPI
from users.views import LoginView, LogoutView
from users.api import UserListAPI, UserDetailAPI

urlpatterns = [
    path('admin/', admin.site.urls),

    # Photos URLS
    path('', HomeView.as_view(), name='photos_home'),
    path('my_photos/', login_required(UserPhotosView.as_view()), name='user_photos'), # Tambien puedes proteger las view mediante las URLs
    path('photos/', PhotoListView.as_view(), name='photos_list'),
    path('photo/<pk>', DetailView.as_view(), name='photo_detail'),
    path('photos/new', CreateView.as_view(), name='create_photo'),

    # Photo API URLs
    path('api/1.0/photos', PhotoListAPI.as_view(), name='photo_list_api'),
    path('api/1.0/photo/<pk>', PhotoDetailAPI.as_view(), name='photo_detail_api'),

    # Users URLS
    path('login', LoginView.as_view(), name='users_login'),
    path('logout', LogoutView.as_view(), name='users_logout'),

    # Users API URLs
    path('api/1.0/users', UserListAPI.as_view(), name='user_list_api'),
    path('api/1.0/users/<pk>', UserDetailAPI.as_view(), name='user_detail_api'),
]
