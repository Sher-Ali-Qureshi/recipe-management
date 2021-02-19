from rest_framework import serializers
from recipe_management_api import models


class HelloSerializer(serializers.Serializer):
    """Serializer a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer a user profile object"""


    class Meta:
            model = models.UserProfile
            fields = ('id', 'email', 'name', 'password')
            extra_kwargs = {
                'password': {
                    'write_only': True,
                    'style': {'input_type': 'password'}
                }
            }


    def create(self, validated_date):
        """Create and return a new user"""
        user =models.UserProfile.objects.create_user(
            email=validated_date['email'],
            name=validated_date['name'],
            password=validated_date['password']
        )
        return user

class UserRecipeSerializer(serializers.ModelSerializer):
    """UserRecipe profile feed items"""

    class Meta:
        model = models.UserRecipe
        fields = ('id', 'user_profile', 'title', 'briefdescription', 'stepwise', 'directions', 'ingredients', 'create_on')
        extra_kwargs = {'user_profile': {
            'read_only': True
        }}

class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True,)
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = models.UserProfile
        fields = ('old_password', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({"old_password": "Old password is not correct"})
        return value

    def update(self, instance, validated_data):

        instance.set_password(validated_data['password'])
        instance.save()

        return instance