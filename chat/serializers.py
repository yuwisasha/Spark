from rest_framework import serializers

from .models import Swipe, Message


class SwipeSirealizer(serializers.ModelSerializer):

    class Meta:
        model = Swipe
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    content = serializers.CharField(required=True)

    class Meta:
        model = Message
        fields = '__all__'
