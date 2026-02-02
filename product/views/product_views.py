from rest_framework.permissions import IsAdminUser, AllowAny
from product.models.product import Product
from product.serializers.product_serializer import ProductSerializer
from rest_framework import generics

class ProductListCreateAPIView(generics.ListCreateAPIView):
  queryset=Product. objects.all()
  serializer_class=ProductSerializer

  def get_permissions(self):
    self.permission_classes= [AllowAny]
    if self.request.method == 'POST':
      self.permission_classes = [IsAdminUser]
    return super().get_permissions()


class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
  queryset=Product. objects.all()
  serializer_class=ProductSerializer

  def get_permissions(self):
    self.permission_classes= [AllowAny]
    if self.request.method in ['PUT', 'PATCH', 'DELETE']:
      self.permission_classes = [IsAdminUser]
    return super().get_permissions()

