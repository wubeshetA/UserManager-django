
from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)
class RequestLog(models.Model):
    method = models.CharField(max_length=10)
    path = models.TextField(blank=True)
    source = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
