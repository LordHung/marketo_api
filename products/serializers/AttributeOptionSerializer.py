from rest_framework import serializers

from ..models import Attribute, Option


class AttributeOptionSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='option-detail')

    class Meta:
        model = Option
        fields = '__all__'

    def to_representation(self, value):
        return value.name
