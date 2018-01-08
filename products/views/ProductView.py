from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.decorators import list_route
from django.utils.datastructures import MultiValueDictKeyError
from django.db.models.query import EmptyQuerySet

from ..models import Product

from ..serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # def create(self, request, *args, **kwargs):
    #     serializer = ProductSerializer(data=request.DATA, files=request.FILES)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=HTTP_201_CREATED)
    #     return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    # @list_route()
    def list(self, request, *args, **kwargs):
        store_id = category_id = None
        queryset = Product.objects.all()
        params = request.query_params
        # print(params)
        try:
            if 'store-id' in params:
                store_id = params['store-id']
                queryset = Product.objects.filter(store_id=store_id)
            elif 'category-id' in params:
                category_id = params['category-id']
                queryset = Product.objects.filter(categories__id=category_id)
            elif 'search' in params:
                search_query = params['search']
                queryset = Product.objects.search(search_query)
        except MultiValueDictKeyError:
            queryset = Product.objects.all()

        # return super(ProductViewSet, self).list(request, *args, **kwargs)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
