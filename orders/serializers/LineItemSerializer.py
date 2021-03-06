from rest_framework import serializers

from ..models import LineItem


class LineItemSerializer(serializers.ModelSerializer):
    total = serializers.SerializerMethodField()
    name = serializers.CharField(source='product.name', read_only=True)

    class Meta:
        model = LineItem
        fields = ('product', 'name', 'quantity', 'total', 'refunded')

    def get_total(self, object):
        try:
            sale_price = object.product.sale_price
            if sale_price:
                return sale_price * object.quantity
            else:
                return object.product.price * object.quantity
        except:
            return 0.0
