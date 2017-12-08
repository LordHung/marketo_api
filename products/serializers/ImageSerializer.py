from rest_framework import serializers
from ..models import Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

    def to_representation(self, value):
        data = super(ImageSerializer, self).to_representation(value)
        return {
            'url': data['image']
        }
