from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    forget_user = models.CharField(max_length=100,blank=False ,default=" ")
    forget_password_token = models.CharField(max_length=255, default="")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.forget_user