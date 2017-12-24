from rest_framework import viewsets
from rest_framework.response import Response

from ..models import Category

from ..serializers import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def list(self, request, *args, **kwargs):
        try:
            store_id = request.GET['store-id']
            queryset = Category.objects.filter(store_id=store_id)
        except:
            queryset = Category.objects.all()

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
