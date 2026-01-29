from django.urls import path
from account.views.account_views import UserDetailAPIView, UserListAPIView, UserMeAPIView

urlpatterns = [
    path('', UserListAPIView.as_view(), name='user-list'),
    path('me/', UserMeAPIView.as_view(), name='user-me'),
    path('<int:pk>/', UserDetailAPIView.as_view(), name='user-detail'),
]