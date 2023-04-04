from django.urls import path, include
from rest_framework.routers import DefaultRouter
from photos.api import PhotoViewSet

# APIRouter
router = DefaultRouter()
router.register('photos', PhotoViewSet)

urlpatterns = [
    # API URLs
    path('1.0/', include(router.urls)), #incluyo las URLs de API
]