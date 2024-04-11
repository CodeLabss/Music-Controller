from .views import Roomview , CreateRoomView
from django.urls import path

urlpatterns = [
    path('room', Roomview.as_view()),
    path('create-room', CreateRoomView.as_view())
]