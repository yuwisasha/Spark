from rest_framework import serializers


from .models import User, Profile, ProfileImage


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


class ProfileImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProfileImage
        fields = ['image', ]


class ProfileSerializer(serializers.ModelSerializer):
    images = ProfileImageSerializer(many=True)

    class Meta:
        model = Profile
        fields = (
            'name', 'date_of_birth', 'gender', 'looking_for',
            'sexual_identity', 'bio', 'interest', 'images',
        )

    def create(self, validated_data):
        images_data = validated_data.pop('images')
        profile = Profile.objects.create(
            name=validated_data['name'],
            date_of_birth=validated_data['date_of_birth'],
            gender=validated_data['gender'],
            looking_for=validated_data['looking_for'],
            sexual_identity=validated_data['sexual_identity'],
            user=validated_data['user'],
        )
        profile.interest.set(validated_data['interest'])
        for image_data in images_data:
            ProfileImage.objects.create(profile=profile, **image_data)
        return profile
