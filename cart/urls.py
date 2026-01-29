from django.urls import path
from cart.views.cart_views import CartListApiView, CartDetailApiView, cart_me

urlpatterns = [
    path('', CartListApiView.as_view(), name='cart-list'),
    path('me/', cart_me, name='cart-me'),
    path('<uuid:pk>/', CartDetailApiView.as_view(), name='cart-detail'),
]