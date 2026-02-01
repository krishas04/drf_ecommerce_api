from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework import generics

from account.serializers.user_serializer import UserSerializer

User = get_user_model()

class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset=User.objects.all()
    serializer_class= UserSerializer

    def get_permissions(self):
        self.permission_classes= [AllowAny]
        if self.request.method == 'POST':
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_me(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)

class UserDetailAPIView(generics.RetrieveAPIView):
    queryset=User.objects.all()
    serializer_class= UserSerializer

