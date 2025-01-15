from django.db import models
import bcrypt


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def set_password(self, raw_password):
        salt = bcrypt.gensalt()
        self.password = bcrypt.hashpw(raw_password, salt)