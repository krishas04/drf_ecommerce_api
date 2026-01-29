from django.urls import path
from account.views.account_views import UserDetailAPIView, UserListAPIView, user_me

urlpatterns = [
    path('', UserListAPIView.as_view(), name='user-list'),
    path('me/', user_me, name='user-me'),
    path('<int:pk>/', UserDetailAPIView.as_view(), name='user-detail'),
]