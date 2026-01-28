from rest_framework import serializers

from product.serializers.product_serializer import ProductSerializer

class ProductInfoSerializer(serializers.Serializer):
  products=ProductSerializer(many=True)
  count=serializers.IntegerField()
  max_price=serializers.FloatField()