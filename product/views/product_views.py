from rest_framework.permissions import IsAdminUser, AllowAny
from product.models.product import Product
from product.pagination import ProductPagination
from product.product_filter import InStockFilterBackend, ProductFilter
from product.serializers.product_serializer import ProductSerializer
from rest_framework import generics
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

class ProductListCreateAPIView(generics.ListCreateAPIView):
  queryset=Product. objects.all()
  serializer_class=ProductSerializer
  filterset_class= ProductFilter
  filter_backends=[
    DjangoFilterBackend,
    filters.SearchFilter,
    filters.OrderingFilter,
    InStockFilterBackend
    ]
  search_fields=['name','description']
  ordering_fields=['name','price','stock']
  ordering='name' #default ordering
  pagination_class=ProductPagination

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

