from rest_framework import serializers

from stores.serializers import StoreSerializer

from ..models import Product, Image, Category, Attribute, Tag
from .AttributeSerializer import AttributeSerializer
from .VariationSerializer import VariationSerializer
from .ImageSerializer import ImageSerializer


class ProductSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='product-detail')
    variation_set = VariationSerializer(many=True, required=False, read_only=True)
    image_set = ImageSerializer(many=True, required=False, read_only=True)
    category_ids = serializers.PrimaryKeyRelatedField(
        many=True, read_only=False, queryset=Category.objects.all(), source='categories')
    # attribute_ids = serializers.PrimaryKeyRelatedField(
    #     many=True, read_only=False, queryset=Attribute.objects.all(), source='attributes')
    attributes = AttributeSerializer(many=True, read_only=True)
    tag_ids = serializers.PrimaryKeyRelatedField(
        many=True, read_only=False, queryset=Tag.objects.all(), source='tags')

    class Meta:
        model = Product
        fields = ('id', 'url', 'store', 'name', 'status', 'price', 'on_sale', 'sale_price', 'image_set',
                'category_ids', 'attributes', 'tag_ids', 'variation_set', 'description', 'short_description', )

    # def create(self, validated_data):
    #     images_data = validated_data.pop('productimage_set')
    #     product = Product.objects.create(**validated_data)
    #     for image_data in images_data:
    #         ProductImage.objects.create(product=product, **image_data)
    #     return product
