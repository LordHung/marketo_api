from django.contrib.auth import get_user_model
from rest_framework import serializers

from accounts.serializers import UserSerializer

from ..models import Store
from products.models import Product, Review
from products.serializers import ProductSerializer

User = get_user_model()


class StoreSerializer(serializers.ModelSerializer):
    active = serializers.BooleanField(initial=True)
    url = serializers.HyperlinkedIdentityField(view_name='store-detail')
    product_count = serializers.IntegerField(source='product_set.count', read_only=True)
    discount_count = serializers.IntegerField(source='get_discounts_count', read_only=True)
    discounts = serializers.SerializerMethodField()
    topratings = serializers.SerializerMethodField()
    topsellers = serializers.SerializerMethodField()

    class Meta:
        model = Store
        fields = ('id', 'url', 'name', 'user', 'icon', 'active', 'product_count',
                  'discount_count', 'discounts', 'topratings', 'topsellers', 'timestamp', 'updated', )

    def get_discounts(self, obj):
        discounts = obj.product_set.filter(on_sale=True)
        return ProductSerializer(discounts, many=True, context={'request': self.context['request']}).data

    def get_topratings(self, obj):
        tr = obj.product_set.order_by('-average_rating')
        return ProductSerializer(tr, many=True, context={'request': self.context['request']}).data

    def get_topsellers(self, obj):
        ts = obj.product_set.order_by('-sold')
        return ProductSerializer(ts, many=True, context={'request': self.context['request']}).data
