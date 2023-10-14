from django.urls import path, include
# import the User model using the setting
from django.contrib.auth import get_user_model 
from django.contrib.auth.hashers import make_password 
from rest_framework import routers, serializers, viewsets
# Serializers define the API representation.


User = get_user_model()
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
