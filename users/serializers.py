# serializers.py
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'second_name', 'phone_number', 'country', 'region', 'is_student', 'is_active', 'is_staff']
        read_only_fields = ['id', 'is_active', 'is_staff']
        
class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'second_name', 'phone_number', 'country', 'region', 'is_student']
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
