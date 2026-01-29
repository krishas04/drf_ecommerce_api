from rest_framework import generics

from orders.models.orders import Order
from orders.serializers.orders_serializer import OrderSerializer

class OrderListAPIView(generics.ListAPIView):
  serializer_class= OrderSerializer

  def get_queryset(self):
    return (
      Order.objects
      .select_related('user')
      .prefetch_related('items__product')
      )
