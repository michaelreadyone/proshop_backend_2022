from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from base.models import Product
from base.serializers import ProductSerializer
import time

from rest_framework import status


@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    print('sleep for 0.3 s')
    time.sleep(0.3)  # test Loading from frontend
    return Response(serializer.data)


@api_view(['GET'])
def getProduct(request, pk):
    product = Product.objects.get(_id=pk)
    serializer = ProductSerializer(product)
    time.sleep(0.3)
    return Response(serializer.data)
