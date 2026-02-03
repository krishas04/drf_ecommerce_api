import django_filters 
from rest_framework import filters

from product.models.product import Product

class ProductFilter(django_filters.FilterSet):
  class Meta:
    model= Product
    fields={
      'name':['exact','icontains'],
      'price':['exact','lt','gt','range']
    }

#Custom generic filtering
class InStockFilterBackend(filters.BaseFilterBackend):
  def filter_queryset(self, request, queryset, view):
    return queryset.filter(stock__gt=0)