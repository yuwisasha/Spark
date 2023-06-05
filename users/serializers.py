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

    def create(self, validated_data):
        profile = Profile.objects.create(
            name=validated_data['name'],
            date_of_birth=validated_data['date_of_birth'],
            gender=validated_data['gender'],
            looking_for=validated_data['looking_for'],
            sexual_identity=validated_data['sexual_identity'],
            user=validated_data['user']
        )
        profile.interest.set(validated_data['interest'])
        return profile

    class Meta:
        model = Profile
        fields = ('name', 'date_of_birth', 'gender',
                  'looking_for', 'sexual_identity', 'bio', 'interest')
