from rest_framework import serializers
from ..models import BillingProfile
from addresses.serializers import AddressSerializer


class BillingProfileSerializer(serializers.ModelSerializer):
    address_set = AddressSerializer(read_only=True, many=True)

    class Meta:
        model = BillingProfile
        # fields = '__all__'
        fields = ('id', 'user', 'customer_id', 'email', 'phone', 'active', 'address_set')
