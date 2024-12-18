from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializer, RegisterUserSerializer
from .models import User

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class RegisterView(APIView):
    serializer_class = RegisterUserSerializer
    def get(self, request, format=None):
        queryset = User.objects.all()

        return Response({'Testing'}, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):

        serializer = self.serializer_class(data=request.data)

        #Check if the request is valid
        if serializer.is_valid():
            #Gets the info from the serializer
            new_username = serializer.data.get('username')
            password = serializer.data.get('password')

            #Checks to see if user exists
            queryset = User.objects.filter(username=new_username)
            if queryset.exists():
                return Response({'User exists'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                newUser = User(username=new_username, password=password)
                newUser.save()


        return Response(RegisterUserSerializer(newUser).data, status=status.HTTP_200_OK)



