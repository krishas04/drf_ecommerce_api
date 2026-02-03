from django_filters import rest_framework as filters

from product.models.product import Product

class ProductFilter(filters.FilterSet):
  class Meta:
    model= Product
    fields={
      'name':['exact','icontains'],
      'price':['exact','lt','gt','range']
    }