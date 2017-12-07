from rest_framework import serializers

from ..models import Variation


class VariationSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='variation-detail')

    class Meta:
        model = Variation
        # fields = ('url', 'id', 'title', 'image', 'price', 'sale_price', 'inventory')
        fields = '__all__'
