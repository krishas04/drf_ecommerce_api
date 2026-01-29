from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.db.models import Prefetch
from rest_framework import generics

from cart.models.cart import Cart
from cart.models.cart_item import CartItem
from cart.serializers.cart_serializer import CartSerializer

class CartListApiView(generics.ListAPIView):
    queryset= Cart.objects.select_related('user').prefetch_related(
                Prefetch(
                    'cart_items',
                    queryset=CartItem.objects.select_related('product')
                    )
                )
    serializer_class=CartSerializer


class CartDetailApiView(generics.RetrieveAPIView):
    queryset= Cart.objects.select_related('user').prefetch_related(
                Prefetch(
                    'cart_items',
                    queryset=CartItem.objects.select_related('product')
                    )
                )
    serializer_class=CartSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def cart_me(request):
    cart = get_object_or_404(
        Cart.objects.select_related('user').prefetch_related(
        Prefetch(
            'cart_items',
            queryset=CartItem.objects.select_related('product')
            )
        ), user=request.user
        )
    serializer = CartSerializer(cart)
    return Response(serializer.data)