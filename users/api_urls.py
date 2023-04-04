from django.urls import path, include

from rest_framework.routers import DefaultRouter
from users.api import UserViewSet

# APIRouter
router = DefaultRouter()
router.register('users', UserViewSet, basename='user')

urlpatterns = [
    # API URLs
    path('1.0/', include(router.urls)), #incluyo las URLs de API
]