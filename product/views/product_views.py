from product.models.product import Product
from product.serializers.product_serializer import ProductSerializer
from rest_framework import generics

class ProductListCreateAPIView(generics.ListCreateAPIView):
  queryset=Product. objects.all()
  serializer_class=ProductSerializer


class ProductDetailAPIView(generics.RetrieveAPIView):
  queryset=Product. objects.all()
  serializer_class=ProductSerializer

