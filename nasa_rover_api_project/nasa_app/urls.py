from django.urls import path
from .views import mars_photos_view

urlpatterns = [
    path('mars/', mars_photos_view, name='mars_photos'),
]
