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

urlpatterns = [
    path('admin/', admin.site.urls),

    # Photos URLS
    path('', views.home, name='photos_home'),
    path('photos/<pk>', views.detail, name='photo_detail'),

    # Users URLS
    path('login', user_view.login, name='users_login'),
    path('logout', user_view.logout, name='users_logout')
]
