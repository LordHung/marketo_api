from rest_framework import viewsets

from ..models import Attribute, Option

from ..serializers import AttributeSerializer, AttributeOptionSerializer


class AttributeViewSet(viewsets.ModelViewSet):
    queryset = Attribute.objects.all()
    serializer_class = AttributeSerializer
