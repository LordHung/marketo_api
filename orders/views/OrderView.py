from rest_framework import viewsets
from rest_framework.parsers import FormParser

from ..models import Order
from ..serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def list(self, request, *args, **kwargs):
        customer_id = None
        queryset = Order.objects.all()
        params = request.query_params
        try:
            if 'customer-id' in params:
                customer_id = params['customer-id']
                queryset = Order.objects.filter(customer=customer_id)
        except MultiValueDictKeyError:
            queryset = Order.objects.all()

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
    	return super(OrderViewSet, self).post(request, *args, **kwargs)
