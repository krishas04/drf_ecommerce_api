from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/',include('product.urls')),
    path('orders/',include('orders.urls')),
    path('accounts/', include('account.urls')),
    path('carts/', include('cart.urls')),
    path('silk/', include('silk.urls', namespace='silk')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
