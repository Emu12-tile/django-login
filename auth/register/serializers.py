from .models import Register
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    # email = serializers.EmailField()

    class Meta:
        model = Register
        fields = ['Name','username', 'email']

    # def validate_email(self, value):
    #     """
    #     Check that the email is not already in use.
    #     """
    #     if User.objects.filter(email=value).exists():
    #         raise serializers.ValidationError("Email is already in use")
    #     return value