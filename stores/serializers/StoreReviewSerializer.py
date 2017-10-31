from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from ..models import StoreReview
from ..serializers import StoreSerializer
from accounts.serializers import UserSerializer


class StoreReviewSerializer(ModelSerializer):
    # user = UserSerializer()
    # store = StoreSerializer()

    class Meta:
        model = StoreReview
        fields = ('user', 'store', 'rating', 'comment', 'approved', 'spam')
