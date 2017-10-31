from django.contrib.auth import get_user_model
from django.forms import ModelChoiceField
from rest_framework import serializers
from ..models import Store
from accounts.serializers import UserSerializer

User = get_user_model()


class StoreSerializer(serializers.ModelSerializer):
    # user = ModelChoiceField(queryset=User.objects.all(), required=True)
    # icon = serializers.FileField(max_length=None, allow_empty_file=True, required=True)
    # icon = serializers.SerializerMethodField()
    # active = serializers.BooleanField(required=False)

    class Meta:
        model = Store
        fields = ('id', 'title', 'user', 'icon', 'active', )
        # fields = '__all__'

    # def get_icon(self, obj):
    #     return obj.icon.name
    #     try:
    #         return obj.icon.url
    #     except:
    #         return None
