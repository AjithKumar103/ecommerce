from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import *
from .serializers import ProductSerializer


@api_view(["GET"])
def productListApi(request, *args, **kwargs):
    queryset = Product.objects.all()
    serializer = ProductSerializer(instance=queryset, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def addToCartApi(request, *args, **kwargs):
    product = Product.objects.get(id=request.data.pid)
    print(product.name)
    return Response(status=status.HTTP_200_OK)
