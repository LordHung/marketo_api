from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
# from accounts.models.User import User

User = get_user_model()


class UserSerializer(ModelSerializer):
    password = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True,  # <- never send password (or hash) to the client
    )

    class Meta:
        model = User
        fields = ('email', 'password', 'full_name')
    
    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            full_name=validated_data['full_name'],
            password=make_password(validated_data['password'])
        )
        return user
