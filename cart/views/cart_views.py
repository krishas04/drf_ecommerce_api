from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from cart.models.cart import Cart
from cart.serializers.cart_serializer import CartSerializer

@api_view(['GET'])
def cart_list(request):
    carts = Cart.objects.all()
    serializer = CartSerializer(carts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def cart_detail(request, pk):
    cart = get_object_or_404(Cart, pk=pk)
    serializer = CartSerializer(cart)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def cart_me(request):
    cart = get_object_or_404(Cart, user=request.user)
    serializer = CartSerializer(cart)
    return Response(serializer.data)