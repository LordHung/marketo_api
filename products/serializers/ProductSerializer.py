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
    average_rating = serializers.SerializerMethodField()
    rating_count = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id', 'url', 'store', 'name', 'status', 'purchasable', 'price', 'on_sale', 'sale_price', 'category_ids',
                  'attributes', 'tag_ids', 'variation_set', 'description', 'average_rating', 'rating_count', 
                  'short_description', 'updated', 'timestamp', 'image_set',)
    
    def get_average_rating(self, obj):
        average_rating = 0.0

        for review in obj.review_set.all():
            average_rating += review.rating
        user_count = obj.review_set.count()
        try:
            return average_rating / user_count
        except ZeroDivisionError:
            return 0.0
    
    def get_rating_count(self, obj):
        return obj.review_set.count()


    # Dùng để post multiple images, impl later
    # def create(self, validated_data):
    #     images_data = validated_data.pop('productimage_set')
    #     product = Product.objects.create(**validated_data)
    #     for image_data in images_data:
    #         ProductImage.objects.create(product=product, **image_data)
    #     return product
