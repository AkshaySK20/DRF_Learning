#from django.http import JsonResponse
import json
from products.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer

@api_view(['POST'])
def api_home(request, *args, **kwargs):

    data = request.data # Take in the data from the POST method
    serializer = ProductSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        print(serializer)
        return Response(serializer.data)
    
    