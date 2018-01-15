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
    # attributes = serializers.PrimaryKeyRelatedField(
    #     many=True, read_only=False, queryset=Attribute.objects.all())
    attributes = AttributeSerializer(many=True, read_only=True)
    tag_ids = serializers.PrimaryKeyRelatedField(
        many=True, read_only=False, queryset=Tag.objects.all(), source='tags')
    rating_count = serializers.IntegerField(source='review_set.count', read_only=True)
    sold = serializers.IntegerField(read_only=True)
    sale_rate = serializers.FloatField(read_only=True)
    average_rating = serializers.FloatField(read_only=True)

    class Meta:
        model = Product
        ordering = ('id',)
        fields = ('id', 'url', 'store', 'name', 'status', 'purchasable', 'price', 'on_sale', 'sale_price', 'sale_rate', 
                  'quantity', 'sold', 'category_ids', 'attributes', 'tag_ids', 'variation_set', 'description', 'average_rating',
                  'rating_count', 'short_description', 'updated', 'timestamp', 'image_set',)
    
    # Dùng để post multiple images, impl later
    # def create(self, validated_data):
    #     images_data = validated_data.pop('productimage_set')
    #     product = Product.objects.create(**validated_data)
    #     for image_data in images_data:
    #         ProductImage.objects.create(product=product, **image_data)
    #     return product
