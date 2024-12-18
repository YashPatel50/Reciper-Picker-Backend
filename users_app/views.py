from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializer
from .models import User

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class RoomView(generics.ListAPIView):
    #What to return
    queryset = User.objects.all()
    #How to convert format 
    serializer_class = UserSerializer

class RegisterView(APIView):
    def get(self, request, format=None):
        return Response({'Testing connection'}, status=status.HTTP_200_OK)



