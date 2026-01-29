from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from rest_framework import generics

from account.serializers.user_serializer import UserSerializer

User = get_user_model()

class UserListAPIView(generics.ListAPIView):
    queryset=User.objects.all()
    serializer_class= UserSerializer

class UserMeAPIView(generics.RetrieveAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=[IsAuthenticated]

    def get_object(self):
        return self.request.user



class UserDetailAPIView(generics.RetrieveAPIView):
    queryset=User.objects.all()
    serializer_class= UserSerializer

