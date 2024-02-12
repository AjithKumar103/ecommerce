from rest_framework import serializers

from .models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "price",
            "type",
            "imageUrl",
        )


class OrderItemSerializer(serializers.ModelSerializer):
    product_item = ProductSerializer(source="product", read_only=True)

    class Meta:
        model = OrderItem
        fields = (
            "id",
            "quantity",
            "get_total",
            "product_item",
        )


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = (
            "id",
            "get_total_order_cost",
            "get_total_order_items",
            "order_items",
        )
