from rest_framework import serializers

from stores.serializers import StoreSerializer

from ..models import Product, ProductImage, Category
from .VariantSerializer import VariantSerializer
# from .CategorySerializer import CategorySerializer


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        # fields = ('id', 'image', )
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='product-detail')
    variant_set = VariantSerializer(many=True, read_only=True, required=False)
    images = ProductImageSerializer(many=True, required=False)
    # images = ProductImageSerializer(required=False)
    # categories = serializers.SlugRelatedField(
    #     many=True,
    #     slug_field='title',
    #     queryset=Category.objects.all()
    # )
    # categories = CategorySerializer(many=True)
    # image = serializers.SerializerMethodField()
    # images = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='product-image-detail'
    # )
    # store = StoreSerializer()

    class Meta:
        model = Product
        fields = ('url', 'id', 'store', 'title', 'images', 'price',
                  'variant_set', 'short_description', 'long_description')
        # fields = '__all__'

    def create(self, validated_data):
        images_data = validated_data.pop('images')
        product = Product.objects.create(**validated_data)
        for image_data in images_data:
            ProductImage.objects.create(product=product, **image_data)
        return product

    # def get_image(self, obj):
    #     # return obj.productimage_set.first().image.url
    #     try:
    #         return obj.productimage_set.first().image.url
    #     except:
    #         return None
