from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = (
            'id', 
            'username', 
            'first_name', 
            'last_name',
            'email', 
            'bio', 
            'birth_date', 
            'avatar',
            'date_joined', 
            'slug',
            'gender', 
            'phone',
            'password'
        )
    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            username=validated_data.get('username', None),
          
        )
        return user
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        if instance.avatar:
            data['avatar'] = 'http://127.0.0.1:8000' + instance.avatar.url
        return data
    
    
class EditUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = (
            'id', 
            'username', 
            'first_name', 
            'last_name',
            'email', 
            'bio', 
            'birth_date', 
            'date_joined', 
            'gender',
            'phone',
            'avatar'
        )

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if instance.avatar:
            data['avatar'] = 'http://127.0.0.1:8000' + instance.avatar.url
        return data

   
    
class ChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(required=True)
