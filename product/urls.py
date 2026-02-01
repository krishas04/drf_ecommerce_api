from django.urls import path

from product.views.category_views import CategoryListCreateAPIView
from product.views.product_info_views import ProductInfoAPIView
from product.views.product_views import ProductListCreateAPIView, ProductDetailAPIView


urlpatterns=[
  path('',ProductListCreateAPIView.as_view(),name="product-list-and-create"),
  path('<int:pk>/',ProductDetailAPIView.as_view(), name="product-detail"),
  path('categories/',CategoryListCreateAPIView.as_view(), name="category-list"),
  path('product_info/',ProductInfoAPIView.as_view(), name="product-info")
]