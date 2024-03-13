from django.shortcuts import render
from rest_framework import generics
from api.models import room
from api.serializers import roomserializer
from api.serializers import *

# Create your views here.
class roomview(generics.CreateAPIView):
    queryset = room.objects.all()
    serializer_class  = roomserializer