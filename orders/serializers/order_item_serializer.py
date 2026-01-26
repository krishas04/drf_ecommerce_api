from rest_framework import serializers

from orders.models.order_item import OrderItem
from product.serializers.product_serializer import ProductSerializer


class OrderItemSerializer(serializers.ModelSerializer):
  product_name = serializers.CharField(source='product.name')
  product_price = serializers.DecimalField(source="product.price", max_digits=10, decimal_places=2)

  class Meta:
    model= OrderItem
    fields= [
      'product_name',
      'product_price',
      'quantity'
    ]
