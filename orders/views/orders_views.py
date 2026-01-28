from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Prefetch

from orders.models.order_item import OrderItem
from orders.models.orders import Order
from orders.serializers.orders_serializer import OrderSerializer

@api_view(['GET'])
def order_list(request):
  orders= Order.objects.select_related('user').prefetch_related(
    Prefetch(
      'items',
      queryset= OrderItem.objects.select_related('product')
    )
  )
  serializer= OrderSerializer(orders,many=True)
  return Response(serializer.data)