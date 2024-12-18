
from rest_framework import serializers
from .models import User

#Used to extract model info
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')