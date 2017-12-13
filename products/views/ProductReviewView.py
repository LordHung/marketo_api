from rest_framework import viewsets
from rest_framework.response import Response

from ..models import Review
from ..serializers import ProductReviewSerializer


class ProductReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ProductReviewSerializer

    def list(self, request, *args, **kwargs):
        try:
            product_id = request.GET['product-id']
            queryset = Review.objects.filter(product_id=product_id)
        except:
            queryset = Review.objects.all()
        
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)