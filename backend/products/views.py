from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from django.http import Http404
from .models import Product
from .serializers import ProductSerializer

class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        
        if content is None:
            content = title

        serializer.save(content=content)
        

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all() # The queryset that should be used for returning objects from this view
    serializer_class = ProductSerializer # The serializer class that should be used for validating and deserializing the data


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        
        if content is None:
            content = title

        serializer.save(content=content)

@api_view(['GET', 'POST'])
def product_alt_view(request, pk=None, *args, **kwargs):
    if request.method == 'GET':
        if pk is not None:
            # detail view
            # queryset = Product.objects.filter(pk=pk)
            # if not queryset.exists():
            #     raise Http404
            # OR We can do it like this..

            obj = get_object_or_404(Product, pk=pk)
            # The above will either get the object or raise http 404 error
            data = ProductSerializer(obj, many=False).data
            return Response(data)

        queryset = Product.objects.all()
        # Serialize the queryset
        data = ProductSerializer(queryset, many=True).data
        return Response(data)

    if request.method == 'POST':
        # Create an item
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
        
            if content is None:
                content = title

            serializer.save(content=content)
        return Response(serializer.data)
    return Response({'Invalid':"Not good data"}, status=400)
    