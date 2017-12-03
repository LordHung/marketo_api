from rest_framework import serializers

from stores.serializers import StoreSerializer

from ..models import Product, ProductImage, Category
from .VariantSerializer import VariantSerializer
from .ProductImageSerializer import ProductImageSerializer


class ProductSerializer(serializers.ModelSerializer):
    # from .CategorySerializer import CategorySerializer
    # url = serializers.HyperlinkedIdentityField(view_name='product-detail')
    variant_set = VariantSerializer(many=True, required=False, read_only=True)
    productimage_set = ProductImageSerializer(many=True, required=False, read_only=True)
    # images = ProductImageSerializer(many=True, required=False, read_only=True)
    # images = serializers.PrimaryKeyRelatedField(many=True, read_only=False, queryset=ProductImage.objects.all(), source='productimage_set')
    category_ids = serializers.PrimaryKeyRelatedField(
        many=True, read_only=False, queryset=Category.objects.all(), source='categories')
    # categories = serializers.SlugRelatedField(
    #     many=True,
    #     slug_field='title',
    #     queryset=Category.objects.all()
    # )
    # categories = CategorySerializer(many=True, required=False, queryset=Category.objects.all())
    # images = serializers.SerializerMethodField()
    # images = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='product-image-detail'
    # )
    # images = serializers.ListField(source='productimage_set.all')
    # images = serializers.CharField(source='productimage_set.all')
    # store = StoreSerializer()
    # images = serializers.SlugRelatedField(
    #     many=True,
    #     read_only=True,
    #     slug_field='',
    #     # queryset=ProductImage.objects.all(),
    #     source='productimage_set.all'
    # )

    class Meta:
        model = Product
        fields = ('id', 'store', 'title', 'price', 'productimage_set',
                  'variant_set', 'category_ids', 'short_description', 'long_description')
        # fields = '__all__'

    # def create(self, validated_data):
    #     images_data = validated_data.pop('images')
    #     product = Product.objects.create(**validated_data)
    #     for image_data in images_data:
    #         ProductImage.objects.create(product=product, **image_data)
    #     return product

    # def update(self, instance, validated_data):
    #     product = Product.objects.get(id=instance.id)
    #     categories_data = validated_data.pop('categories')
    #     for category_data in categories_data:
    #         Category.objects.update(product=product, **category_data)
    #     Product.objects.update(**validated_data)
    #     return product

    # def get_images(self, obj):
    #     # return obj.productimage_set.first().image.url
    #     try:
    #         # return obj.productimage_set.first().image.url
    #         return obj.productimage_set.all()
    #     except:
    #         return None
