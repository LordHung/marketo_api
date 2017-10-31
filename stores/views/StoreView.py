from django.contrib import messages
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework import status, permissions, parsers, response, generics
from rest_framework.response import Response
from ..serializers import StoreSerializer, StoreReviewSerializer
from ..models import Store, StoreReview
from src import filter_backends


class StoreAPIView(APIView):
    filter_backends = (filter_backends.StoreFilterBackend, )
    # parser_classes = (parsers.FormParser, parsers.MultiPartParser)
    # queryset = Store.objects.all()
    # serializer_class = StoreSerializer

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
        # image = request_processing.add_image2(request)
        # return super(StoreAPIView, self).post(self, *args, **kwargs)
        serializer = StoreSerializer()
        messages.success(request, 'Image uploaded successfully.')
        return response.Response(serializer.data, status=status.HTTP_201_CREATED)


class StoreViewSet(ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )


class StoreRVViewSet(ModelViewSet):
    queryset = StoreReview.objects.all()
    serializer_class = StoreReviewSerializer
    # permission_classes
