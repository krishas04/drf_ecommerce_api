from rest_framework import serializers
from cart.models.cart import Cart
from cart.serializers.cart_item_serializer import CartItemSerializer

class CartSerializer(serializers.ModelSerializer):
    # Using 'cartitem_set' because it's the default reverse relation as related_name is not specified in CartItem model
    items = CartItemSerializer(source='cart_items', many=True, read_only=True)
    total_price = serializers.SerializerMethodField()
    user_name=serializers.CharField(source='user.username')

    class Meta:
        model = Cart
        fields = [
            'cart_id',
            'user_name',
            'items',
            'total_price',
            'created_at'
        ]

    def get_total_price(self, obj):
        items = obj.cart_items.all()
        return sum(item.product.price * item.quantity for item in items)