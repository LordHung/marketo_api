from django.contrib.auth import get_user_model
from rest_framework import serializers

from accounts.serializers import UserSerializer

from ..models import Store
from products.models import Product, Review, Image
from products.serializers import ProductSerializer, ImageSerializer

User = get_user_model()


class StoreSerializer(serializers.ModelSerializer):
    active = serializers.BooleanField(initial=True)
    url = serializers.HyperlinkedIdentityField(view_name='store-detail')
    product_count = serializers.IntegerField(source='product_set.count', read_only=True)
    discount_count = serializers.IntegerField(source='get_discounts_count', read_only=True)
    discounts = serializers.SerializerMethodField()
    topratings = serializers.SerializerMethodField()
    topsellers = serializers.SerializerMethodField()
    featured_images = serializers.SerializerMethodField()

    class Meta:
        model = Store
        fields = ('id', 'url', 'name', 'user', 'icon', 'active', 'product_count',
                  'discount_count', 'discounts', 'topratings', 'topsellers', 'timestamp', 'updated', 'featured_images')

    def get_discounts(self, obj):
        discounts = obj.product_set.filter(on_sale=True).order_by('-sale_rate')
        return ProductSerializer(discounts, many=True, context={'request': self.context['request']}).data

    def get_topratings(self, obj):
        tr = obj.product_set.filter(average_rating__gte=4).order_by('-average_rating')
        return ProductSerializer(tr, many=True, context={'request': self.context['request']}).data

    def get_topsellers(self, obj):
        ts = obj.product_set.filter(sold__gte=1).order_by('-sold')
        return ProductSerializer(ts, many=True, context={'request': self.context['request']}).data

    def get_featured_images(self, obj):
        try:
            featured_dc = obj.product_set.filter(on_sale=True).order_by('-sale_rate').first().image_set.all()[:1]
        except:
            featured_dc = Image.objects.none()
        try:
            featured_tr = obj.product_set.filter(average_rating__gte=4).order_by('-average_rating').first().image_set.all()[:1]
        except:
            featured_tr = Image.objects.none()
        try:
            featured_ts = obj.product_set.filter(sold__gte=1).order_by('-sold').first().image_set.all()[:1]
        except:
            featured_ts = Image.objects.none()

        featured_images = featured_dc.union(featured_tr, featured_ts, all=True)

        return ImageSerializer(featured_images, many=True, context={'request': self.context['request']}).data
