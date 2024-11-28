from django.shortcuts import render
from rest_framework import generics
from .serializers import RoomSerializer
from recipe_app.models import Room

# Create your views here.

class RoomView(generics.ListAPIView):
    #What to return
    queryset = Room.objects.all()
    #How to convert format 
    serializer_class = RoomSerializer