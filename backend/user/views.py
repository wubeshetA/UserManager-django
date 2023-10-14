from django.shortcuts import render
from .serializers import UserSerializer
from rest_framework import viewsets
from rest_framework import permissions
from django.contrib.auth import get_user_model
# Create your views here.
# ViewSets define the view behavior.
User = get_user_model()
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    permission_classes = [permissions.AllowAny]
    read_only = False
    