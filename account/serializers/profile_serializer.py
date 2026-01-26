from rest_framework import serializers
from account.models.profile import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'phone_number', 
            'address', 
            'city', 
            'country', 
            'profile_picture'
        ]