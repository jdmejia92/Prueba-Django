from django.urls import path
from django.contrib.auth.decorators import login_required
from photos.views import HomeView, DetailView, CreateView, PhotoListView, UserPhotosView

urlpatterns = [
    # Photos URLS
    path('', HomeView.as_view(), name='photos_home'),
    path('my_photos/', login_required(UserPhotosView.as_view()), name='user_photos'), # Tambien puedes proteger las view mediante las URLs
    path('photos/', PhotoListView.as_view(), name='photos_list'),
    path('photo/<pk>', DetailView.as_view(), name='photo_detail'),
    path('photos/new', CreateView.as_view(), name='create_photo'),
]