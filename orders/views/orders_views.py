from django.db.models import Prefetch
from rest_framework import generics

from orders.models.order_item import OrderItem
from orders.models.orders import Order
from orders.serializers.orders_serializer import OrderSerializer

class OrderListAPIView(generics.ListAPIView):
  queryset= Order.objects.select_related('user').prefetch_related(
    Prefetch(
      'items',
      queryset= OrderItem.objects.select_related('product')
    )
  )
  serializer_class= OrderSerializer
