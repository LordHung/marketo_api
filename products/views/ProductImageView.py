from rest_framework import viewsets

from ..models import ProductImage
from ..serializers import ProductImageSerializer


class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
