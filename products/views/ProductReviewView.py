from rest_framework import viewsets

from ..models import Review
from ..serializers import ProductReviewSerializer


class ProductReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ProductReviewSerializer
