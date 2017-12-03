from rest_framework import serializers

from stores.serializers import StoreSerializer

from ..models import Product, ProductImage, Category
from .VariantSerializer import VariantSerializer
from .ProductImageSerializer import ProductImageSerializer


class ProductSerializer(serializers.ModelSerializer):
    # from .CategorySerializer import CategorySerializer
    # url = serializers.HyperlinkedIdentityField(view_name='product-detail', lookup_field='title')
    variant_set = VariantSerializer(many=True, required=False, read_only=True)
    productimage_set = ProductImageSerializer(many=True, required=False, read_only=False)
    category_ids = serializers.PrimaryKeyRelatedField(
        many=True, read_only=False, queryset=Category.objects.all(), source='categories')

    class Meta:
        model = Product
        fields = ('id', 'url', 'store', 'title', 'price', 'productimage_set',
                  'variant_set', 'category_ids', 'short_description', 'long_description')

    def create(self, validated_data):
        images_data = validated_data.pop('productimage_set')
        product = Product.objects.create(**validated_data)
        for image_data in images_data:
            ProductImage.objects.create(product=product, **image_data)
        return product
