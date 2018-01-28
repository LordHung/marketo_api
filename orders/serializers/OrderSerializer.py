from decimal import Decimal
from rest_framework import serializers
from html_json_forms.serializers import JSONFormSerializer

from ..models import Order, LineItem
from products.models import Product
from .LineItemSerializer import LineItemSerializer


class OrderSerializer(serializers.ModelSerializer, ):
    lineitem_set = LineItemSerializer(many=True)
    url = serializers.HyperlinkedIdentityField(view_name='order-detail')

    class Meta:
        model = Order
        fields = ('id', 'url', 'customer', 'active', 'status', 'billing_address', 'shipping_address', 'payment_method',
                  'payment_method_title', 'shipping_total', 'total', 'currency', 'customer_note',
                  'timestamp', 'updated', 'lineitem_set', )

    def create(self, validated_data):
        lineitems = validated_data.pop('lineitem_set')
        print(validated_data)
        total = Decimal(0.00)
        for item in lineitems:
            prod = item['product']
            print(item['quantity'])
            if prod.on_sale:
                total += prod.sale_price * Decimal(item['quantity'])
            else:
                total += prod.price * Decimal(item['quantity'])
            print(total)

        print(total)
        order = Order.objects.create(**validated_data, total=total)

        for lineitem in lineitems:
            LineItem.objects.create(order=order, **lineitem)
        return order
