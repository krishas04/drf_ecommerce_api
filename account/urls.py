from django.urls import path
from account.views.account_views import UserDetailAPIView, UserListCreateAPIView, user_me

urlpatterns = [
    path('', UserListCreateAPIView.as_view(), name='user-list-and-create'),
    path('me/', user_me, name='user-me'),
    path('<int:pk>/', UserDetailAPIView.as_view(), name='user-detail'),
]