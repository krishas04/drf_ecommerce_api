from django.urls import path

from product.views.category_views import category_list
from product.views.product_views import product_list, product_detail


urlpatterns=[
  path('',product_list, name="product-list"),
  path('<int:pk>/',product_detail, name="product-detail"),
  path('categories/',category_list, name="category-list")
]