from django.contrib.auth import get_user_model
from rest_framework import viewsets
from src.permissions import IsAccountOwnerOrNoModify
# from rest_framework.permissions import (IsAuthenticated, IsAdminUser)
from accounts.serializers import UserSerializer

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-pk')
    serializer_class = UserSerializer
    permission_classes = (IsAccountOwnerOrNoModify, )

    # def get_permissions(self):
    #     # Your logic should be all here
    #     if self.request.method == 'GET':
    #         self.permission_classes = [, ]
    #     else:
    #         self.permission_classes = [IsAuthenticated, ]

    #     return super(UsersViewSet, self).get_permissions()
