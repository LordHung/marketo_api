from rest_framework import serializers
from ..models import WishList


class WishListSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='wishlist-detail')

    class Meta:
        model = WishList
        fields = '__all__'
