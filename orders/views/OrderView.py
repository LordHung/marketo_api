from rest_framework import viewsets
from rest_framework.parsers import FormParser

from ..models import Order
from ..serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # parser_classes = (FormParser, )

    def post(self, request, *args, **kwargs):
    	print(self.request)
    	return super(OrderViewSet, self).list(request, *args, **kwargs)
