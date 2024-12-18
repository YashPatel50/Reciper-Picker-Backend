from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)