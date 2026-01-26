from django.urls import path
from cart.views.cart_views import cart_list, cart_detail, cart_me

urlpatterns = [
    path('', cart_list, name='cart-list'),
    path('me/', cart_me, name='cart-me'),
    path('<uuid:pk>/', cart_detail, name='cart-detail'),
]