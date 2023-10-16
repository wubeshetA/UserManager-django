from django.shortcuts import render
from django.contrib.auth import get_user_model

from rest_framework import viewsets
from rest_framework import permissions
from .models import RequestLog
from .serializers import RequestLogSerializer, UserSerializer
from .consumers import UserConsumer  # Import the UserConsumer

User = get_user_model()
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    permission_classes = [permissions.AllowAny]
    read_only = False
    # access the request object in the serializer
    def get_serializer_context(self):
        return {'request': self.request}

class RequestLogViewSet(viewsets.ModelViewSet):
    
    queryset = RequestLog.objects.all()
    serializer_class = RequestLogSerializer
    
    permission_classes = [permissions.AllowAny]
    read_only = False
    # access the request object in the serializer
    def get_serializer_context(self):
        return {'request': self.request}
    