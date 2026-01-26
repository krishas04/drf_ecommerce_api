from rest_framework import serializers

from product.models.product import Product

class ProductSerializer(serializers.ModelSerializer):
  class Meta:
    model= Product
    fields= [
      'id',
      'name',
      'description',
      'price',
      'stock',
      'category'
    ]

    def validate_price(self, value):
      if value <= 0 :
        raise serializers.ValidationError("Price must be greater than zero.")
      return value