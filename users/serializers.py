from rest_framework import serializers

from .models import User, Profile, ProfileImage, Interest


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


class InterestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Interest
        fields = '__all__'


class ProfileImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProfileImage
        fields = ['image', ]


class ProfileSerializer(serializers.ModelSerializer):
    images = ProfileImageSerializer(
        many=True,
        read_only=True,
        source='profileimage_set',
    )
    # to be able to upload several images at the same time
    # and have them in validated_data
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(allow_empty_file=False, use_url=False),
        write_only=True,
    )

    class Meta:
        model = Profile
        fields = (
            'user_id', 'id', 'name', 'date_of_birth',
            'age', 'gender', 'looking_for',
            'sexual_identity', 'bio', 'interest',
            'images', 'uploaded_images',
        )

    def create(self, validated_data):
        images_data = validated_data.pop('uploaded_images')
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
            ProfileImage.objects.create(profile=profile,
                                        image=image_data,)
        return profile
