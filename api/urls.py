from .views import roomview
from django.urls import path

urlpatterns = [
    path('room', roomview.as_view())
]