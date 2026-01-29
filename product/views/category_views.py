from rest_framework import generics

from product.models.category import Category
from product.serializers.category_serializers import CategorySerializer

class CategoryListAPIView(generics.ListAPIView):
  queryset= Category.objects.all()
  serializer_class= CategorySerializer
