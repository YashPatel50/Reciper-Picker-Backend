from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
import bcrypt


# Create your models here.
class CustomeUserManager(UserManager):
    def _create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError("No Valid Username")
        
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_user(self, username, password, **extra_fields):
        return self._create_user(username, password, **extra_fields)
        

    

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=20, unique=True)

    objects = CustomeUserManager()

    USERNAME_FIELD = 'username'