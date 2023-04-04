from django.urls import path
from users.views import LoginView, LogoutView

urlpatterns = [
    # Users URLS
    path('login', LoginView.as_view(), name='users_login'),
    path('logout', LogoutView.as_view(), name='users_logout'),
]