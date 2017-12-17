from rest_framework import serializers

from ..models import Review


class ProductReviewSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='review-detail')
    user_name = serializers.CharField(source='user.full_name', read_only=True)

    class Meta:
        model = Review
        # fields = '__all__'
        fields = ('url', 'id', 'user', 'user_name', 'product_id', 'rating', 'comment', 'updated')
