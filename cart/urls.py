from django.urls import path
from cart.views.cart_views import CartListApiView, CartDetailApiView, CartMeAPIView

urlpatterns = [
    path('', CartListApiView.as_view(), name='cart-list'),
    path('me/', CartMeAPIView.as_view(), name='cart-me'),
    path('<uuid:pk>/', CartDetailApiView.as_view(), name='cart-detail'),
]