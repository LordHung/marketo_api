from django.contrib.auth import get_user_model
from rest_framework import serializers

from accounts.serializers import UserSerializer

from ..models import Store

User = get_user_model()


class StoreSerializer(serializers.ModelSerializer):
    active = serializers.BooleanField(initial=True)
    url = serializers.HyperlinkedIdentityField(view_name='store-detail')
    product_count = serializers.IntegerField(source='product_set.count')

    class Meta:
        model = Store
        fields = ('id', 'url', 'name', 'user', 'icon', 'active', 'product_count', 'timestamp', 'updated' )
