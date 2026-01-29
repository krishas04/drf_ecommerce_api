from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework import generics

from cart.models.cart import Cart
from cart.serializers.cart_serializer import CartSerializer

class CartListApiView(generics.ListAPIView):
    serializer_class=CartSerializer

    def get_queryset(self):
        return (
            Cart.objects
            .select_related('user')
            .prefetch_related(
                    'cart_items__product'
                )
        )


class CartDetailApiView(generics.RetrieveAPIView):
    serializer_class=CartSerializer

    def get_queryset(self):
        return (
            Cart.objects
            .select_related('user')
            .prefetch_related(
                    'cart_items__product'
                )
        )

class CartMeAPIView(generics.RetrieveAPIView):
    serializer_class= CartSerializer
    permission_classes= [IsAuthenticated]

    def get_object(self):
        return get_object_or_404(
            Cart.objects
            .select_related('user')
            .prefetch_related('cart_items__product')
        )

