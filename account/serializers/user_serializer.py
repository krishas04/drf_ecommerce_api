from rest_framework import serializers
from django.contrib.auth import get_user_model
from account.serializers.profile_serializer import ProfileSerializer

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    # Nesting the profile serializer to show profile data with user data
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = [
            'username', 
            'email', 
            'first_name', 
            'last_name', 
            'profile'
        ]