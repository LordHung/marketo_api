from django.contrib.auth import get_user_model
from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.serializers import AuthTokenSerializer
 
User = get_user_model()

 
#
# Custom token Auth class subclass from DRF framework
#
class TokenAuthView(viewsets.ModelViewSet, ObtainAuthToken):
    '''
    Authenticate user for access token
    '''
    queryset = User.objects.all()
    serializer_class = AuthTokenSerializer
 
    def create(self, request, *args, **kwargs):
        response = super(TokenAuthView, self).post(request, *args, **kwargs)
        response.data['token'] = ' '.join(['Token', response.data['token']])
        return response
 
 
class Logout(APIView):
    queryset = User.objects.all()
 
    def get(self, request, format=None):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
 