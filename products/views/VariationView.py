from rest_framework import viewsets

from ..models import Variation

from ..serializers import VariationSerializer


class VariationViewSet(viewsets.ModelViewSet):
    queryset = Variation.objects.all()
    serializer_class = VariationSerializer
