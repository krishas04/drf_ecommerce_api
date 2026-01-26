from rest_framework import serializers

from orders.models.orders import Order
from orders.serializers.order_item_serializer import OrderItemSerializer

class OrderSerializer(serializers.ModelSerializer):
  items=OrderItemSerializer(many=True, read_only=True)
  total_price=serializers.SerializerMethodField(method_name='total')
  user_name=serializers.CharField(source='user.username')

  def total(self,obj):
    order_items=obj.items.all()
    return sum(order_item.item_subtotal for order_item in order_items)

  class Meta:
    model= Order
    fields= [
      'order_id',
      'created_at',
      'user_name',
      'status',
      'items',
      'total_price'
    ]
