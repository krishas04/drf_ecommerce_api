from rest_framework.decorators import api_view
from rest_framework.response import Response

from orders.models.orders import Order
from orders.serializers.orders_serializer import OrderSerializer

@api_view(['GET'])
def order_list(request):
  orders= Order.objects.all()
  serializer= OrderSerializer(orders,many=True)
  return Response(serializer.data)