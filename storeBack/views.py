from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
import json

from .models import *
from .serializers import ProductSerializer, OrderSerializer, OrderItemSerializer


@api_view(["GET"])
def productListApi(request, *args, **kwargs):
    queryset = Product.objects.all()
    serializer = ProductSerializer(instance=queryset, many=True)
    return Response(serializer.data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def addToCartApi(request, *args, **kwargs):
    if request.user != "AnonymousUser":
        data = json.loads(request.body)
        id, action = data.get("pid"), data.get("action")

        product = Product.objects.get(id=id)
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        order_item, created = OrderItem.objects.get_or_create(
            order=order, product=product
        )

        if action == "add":
            order_item.quantity += 1
        elif action == "remove":
            order_item.quantity -= 1
        order_item.save()

        if order_item.quantity <= 0:
            order_item.delete()
    else:
        print("user not authenticated")
    return Response(status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def cartListApi(request, *args, **kwargs):
    if request.user != "AnonymousUser":
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        serializer = OrderSerializer(instance=order)
        return Response(serializer.data)
