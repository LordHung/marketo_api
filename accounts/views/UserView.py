from django.contrib.auth import get_user_model
from rest_framework import viewsets
from src.permissions import IsAccountOwnerOrNoModify
from accounts.serializers import UserSerializer

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-pk')
    serializer_class = UserSerializer
    permission_classes = (IsAccountOwnerOrNoModify, )
