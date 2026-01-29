from django.urls import path

from orders.views.orders_views import OrderListAPIView

urlpatterns=[
  path('',OrderListAPIView.as_view(), name="order-list")
]