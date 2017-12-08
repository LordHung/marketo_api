from django.contrib import messages
from rest_framework import generics, parsers, response, status
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from src import filter_backends
from src.permissions import IsStoreOwnerOrNoModify

from ..models import Store, StoreReview
from ..serializers import StoreReviewSerializer, StoreSerializer


class StoreAPIView(APIView):
    filter_backends = (filter_backends.StoreFilterBackend, )

    def post(self, request, *args, **kwargs):
        """
        Add image
        ---
        parameters:
            - name: icon
              description: file is used for adding image
              required: true
              type: file
        """
        serializer = StoreSerializer()
        messages.success(request, 'Image uploaded successfully.')
        return response.Response(serializer.data, status=status.HTTP_201_CREATED)


class StoreViewSet(ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class StoreReviewViewSet(ModelViewSet):
    queryset = StoreReview.objects.all()
    serializer_class = StoreReviewSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
