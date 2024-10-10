from .models import RegisterE
from rest_framework import serializers
from django.contrib.auth.models  import User 

class UserSerializer(serializers.ModelSerializer):
    # email = serializers.EmailField()

    class Meta:
        model = RegisterE
        fields = ['Name','username', 'email']

    # def validate_email(self, value):
    #     """
    #     Check that the email is not already in use.
    #     """
    #     if User.objects.filter(email=value).exists():
    #         raise serializers.ValidationError("Email is already in use")
    #     return value

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']  # Add any other fields you want to use
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        # Create a new user with the validated data
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

from django.contrib.auth import authenticate
from rest_framework import serializers

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise serializers.ValidationError("Invalid credentials")
        else:
            raise serializers.ValidationError("Both username and password are required")

        data['user'] = user
        return data
