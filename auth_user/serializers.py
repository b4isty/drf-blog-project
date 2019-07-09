from rest_framework import serializers
from django.contrib.auth import get_user_model
# from .models import CustomUser


class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    # confirm_password = serializers.CharField(style={'input_type': 'password'})

    class Meta:
        model = get_user_model()
        fields = ['email', 'first_name', 'last_name', 'password', ]

    def create(self, validated_data):
        # password = validated_data.get('password')
        user = get_user_model().objects.create_user(**validated_data)
        # user.set_password(password)
        return user

    # def validate(self, data):
    #     """
    #     Check validation of password
    #     """
    #     password = data.get('password')
    #     confirm_password = data.pop('confirm_password', None)
    #     print("&&&&&&&&&", password, confirm_password)
    #     if password and confirm_password and password == confirm_password:
    #
    #         return data
    #     raise serializers.ValidationError("Password doesn't match")
    #
