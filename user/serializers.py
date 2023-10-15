from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from .models import RequestLog 

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password']
        
        
    def __init__(self, *args, **kwargs):
        super(UserSerializer, self).__init__(*args, **kwargs)

        request = self.context.get('request', None)
        if request and (request.method in ['POST', 'PUT']):
            # Remove only 'id' field for POST and PUT requests
            self.fields.pop('id', None)
        
            
    def to_representation(self, instance):
        # Include 'id' field when data is being prepared for rendering
            rep = super(UserSerializer, self).to_representation(instance)
            rep['id'] = instance.id
            # Remove 'password' field when data is being prepared for rendering
            rep.pop('password', None)
       
            return rep

    def validate_password(self, value):
        return make_password(value)
    
    def update(self, instance, validated_data):
        
        # Make password field optional for PUT request
        password = validated_data.pop('password', None)
        
        if password is not None:
            instance.set_password(password)
        
        return super(UserSerializer, self).update(instance, validated_data)
    
class RequestLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestLog
        fields = ['method', 'path', 'created_at', 'source']
