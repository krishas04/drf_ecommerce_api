from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAdminUser

from product.models.category import Category
from product.pagination import CategoryPagination
from product.serializers.category_serializers import CategorySerializer

class CategoryListCreateAPIView(generics.ListCreateAPIView):
  queryset= Category.objects.all()
  serializer_class= CategorySerializer
  pagination_class= CategoryPagination

  def get_permissions(self):
    self.permission_classes= [AllowAny]
    if self.request.method == 'POST':
      self.permission_classes = [IsAdminUser]
    return super().get_permissions()
