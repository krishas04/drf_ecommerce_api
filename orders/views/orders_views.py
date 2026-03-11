from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from orders.models.order_item import OrderItem
from orders.models.orders import Order
from orders.serializers.orders_serializer import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
  queryset= Order.objects.prefetch_related('items__product')
  serializer_class=OrderSerializer
  permission_classes= [AllowAny]


# class OrderListAPIView(generics.ListAPIView):
#   queryset= Order.objects.select_related('user').prefetch_related(
#     Prefetch(
#       'items',
#       queryset= OrderItem.objects.select_related('product')
#     )
#   )
#   serializer_class= OrderSerializer
