from rest_framework import serializers
from cart.models.cart import Cart
from cart.serializers.cart_item_serializer import CartItemSerializer

class CartSerializer(serializers.ModelSerializer):
    # Using 'cartitem_set' because it's the default reverse relation as related_name is not specified in CartItem model
    items = CartItemSerializer(source='cartitem_set', many=True, read_only=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = [
            'cart_id',
            'user',
            'items',
            'total_price',
            'created_at'
        ]

    def get_total_price(self, obj):
        items = obj.cartitem_set.all()
        return sum(item.product.price * item.quantity for item in items)