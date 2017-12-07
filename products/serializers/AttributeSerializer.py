from rest_framework import serializers

from ..models import Attribute
from .AttributeOptionSerializer import AttributeOptionSerializer


class AttributeSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='attribute-detail')
    option_set = AttributeOptionSerializer(many=True, required=False, read_only=True)

    class Meta:
        model = Attribute
        # fields = '__all__'
        fields = ('id', 'url', 'name', 'option_set')
