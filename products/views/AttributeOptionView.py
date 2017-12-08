from rest_framework import viewsets

from ..models import Attribute, Option

from ..serializers import AttributeSerializer, AttributeOptionSerializer


class AttributeOptionViewSet(viewsets.ModelViewSet):
    queryset = Option.objects.all()
    serializer_class = AttributeOptionSerializer
