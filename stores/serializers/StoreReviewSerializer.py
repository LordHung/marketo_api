from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from accounts.serializers import UserSerializer

from ..models import StoreReview
from ..serializers import StoreSerializer


class StoreReviewSerializer(ModelSerializer):
    # user = UserSerializer()
    # store = StoreSerializer()

    class Meta:
        model = StoreReview
        fields = ('user', 'store', 'rating', 'comment', 'approved', 'spam')
