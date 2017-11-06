from rest_framework import serializers

from ..models import Category

from .ProductSerializer import ProductSerializer


class CategorySerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='category-detail')
    product_set = ProductSerializer(many=True, read_only=True)
    
    class Meta:
        model = Category
        # fields = ('url', 'id', 'title', 'description', 'product_set', )
        fields = '__all__'
