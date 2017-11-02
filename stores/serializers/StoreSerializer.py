from django.contrib.auth import get_user_model
from django.forms import ModelChoiceField
from rest_framework import serializers

from accounts.serializers import UserSerializer

from ..models import Store

User = get_user_model()


class StoreSerializer(serializers.ModelSerializer):
    # user = ModelChoiceField(queryset=User.objects.all(), required=True)
    active = serializers.BooleanField(initial=True)
    url = serializers.HyperlinkedIdentityField(view_name='store-detail')
    # user = serializers.CharField(source='user.email')

    class Meta:
        model = Store
        fields = ('id', 'url', 'title', 'user', 'icon', 'active', )
