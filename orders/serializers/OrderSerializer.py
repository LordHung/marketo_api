from rest_framework import serializers
from html_json_forms.serializers import JSONFormSerializer

from ..models import Order, LineItem
from .LineItemSerializer import LineItemSerializer


class OrderSerializer(serializers.ModelSerializer, ):
    lineitem_set = LineItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ('id', 'customer', 'active', 'status', 'billing_address', 'shipping_address', 'payment_method',
                  'payment_method_title', 'shipping_total', 'total', 'currency', 'customer_note', 'lineitem_set', )

    def create(self, validated_data):
        lineitems = validated_data.pop('lineitem_set')
        order = Order.objects.create(**validated_data)
        for lineitem in lineitems:
            LineItem.objects.create(order=order, **lineitem)
        return order
