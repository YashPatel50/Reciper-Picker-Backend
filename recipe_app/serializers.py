
from rest_framework import serializers
from .models import Room

#Used to extract model info
class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'code', 'host', 'guests_can_pause', 'votes_to_skip', 'created_at')

