from django.urls import path
from account.views.account_views import user_detail, user_list, user_me

urlpatterns = [
    path('', user_list, name='user-list'),
    path('me/', user_me, name='user-me'),
    path('<int:pk>/', user_detail, name='user-detail'),
]