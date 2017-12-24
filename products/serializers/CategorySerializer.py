from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField

from ..models import Category

from .ProductSerializer import ProductSerializer


class CategorySerializer(ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='category-detail')
    product_set = ProductSerializer(many=True, read_only=True)
    product_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Category
        fields = ('url', 'id', 'name', 'active', 'store', 'parent', 'product_count',
                  'image', 'description', 'timestamp', 'product_set', )

    def get_product_count(self, obj):
        product_count = 0

        if obj.parent:  # its a subcategory
            product_count = obj.product_set.count()
            return product_count
        else:  # its a main category
            # count products in subcategory
            for category in Category.objects.filter(id__in=[obj.id, obj.parent]).distinct():
                product_count += category.product_set.count()
            return product_count
