from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField

from ..models import Category

from .ProductSerializer import ProductSerializer


class CategorySerializer(ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='category-detail')
    # product_set = ProductSerializer(many=True, read_only=True)
    
    class Meta:
        model = Category
        # fields = ('url', 'id', 'title', 'description', 'product_set', )
        fields = '__all__'
