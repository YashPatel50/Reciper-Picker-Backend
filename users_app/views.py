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
        
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):

        serializer = self.serializer_class(data=request.data)

        #Check if the request is valid
        if serializer.is_valid():
            #Gets the info from the serializer
            new_username = serializer.validated_data.get('username')
            password = serializer.validated_data.get('password')

            #Checks to see if user exists
            queryset = User.objects.filter(username=new_username)
            if queryset.exists():
                return Response({'User exists'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                newUser = User(username=new_username)
                newUser.set_password(raw_password=password)
                newUser.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        return Response(RegisterUserSerializer(newUser).data, status=status.HTTP_200_OK)



