from rest_framework import serializers
from .models import User, Profile


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'password', )
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class ProfileSerializer(serializers.ModelSerializer):

    def create(self, validated_date):
        profile = Profile.objects.create(**validated_date)
        return profile

    class Meta:
        model = Profile
        fields = '__all__'
