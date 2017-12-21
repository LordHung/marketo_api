from rest_framework import serializers
from ..models import BillingProfile


class BillingProfileSerializer(serializers.ModelSerializer):
    # email = serializers.EmailField(default='user.email')
    # url = serializers.HyperlinkedIdentityField(view_name='billings:billing-detail')

    class Meta:
        model = BillingProfile
        # fields = '__all__'
        fields = ('id', 'user', 'customer_id', 'email', 'phone', 'active', 'address_set')
