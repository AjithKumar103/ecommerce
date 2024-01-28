from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import *
from .serializers import ProductSerializer


@api_view(["GET"])
def product_list_api(request, *args, **kwargs):
    queryset = Product.objects.all()
    serializer = ProductSerializer(instance=queryset, many=True)
    return Response(serializer.data)
