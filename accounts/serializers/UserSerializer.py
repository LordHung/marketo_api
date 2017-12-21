from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from billings.serializers import BillingProfileSerializer
from addresses.serializers import AddressSerializer


User = get_user_model()


class UserSerializer(ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='user-detail')
    password = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True,  # <- never send password (or hash) to the client
    )
    billing = BillingProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = ('url', 'email', 'password', 'full_name', 'phone', 'billing')
    
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(UserSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        print(validated_data)
        validated_data['password'] = make_password(validated_data['password'])
        return super(UserSerializer, self).update(instance, validated_data)
