from django.urls import path

from orders.views.orders_views import order_list

urlpatterns=[
  path('',order_list, name="order-list")
]