from rest_framework import serializers

from ..models import Variant


class VariantSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='variant-detail')

    class Meta:
        model = Variant
        # fields = ('url', 'id', 'title', 'image', 'price', 'sale_price', 'inventory')
        fields = '__all__'
