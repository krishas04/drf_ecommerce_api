from django.urls import path

from product.views.category_views import CategoryListAPIView
from product.views.product_info_views import ProductInfoAPIView
from product.views.product_views import ProductListAPIView, ProductDetailAPIView


urlpatterns=[
  path('',ProductListAPIView.as_view(),name="product-list"),
  path('<int:pk>/',ProductDetailAPIView.as_view(), name="product-detail"),
  path('categories/',CategoryListAPIView.as_view(), name="category-list"),
  path('product_info/',ProductInfoAPIView.as_view(), name="product-info")
]