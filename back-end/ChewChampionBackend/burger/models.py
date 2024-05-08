from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

#Currently discovering designing models and authentication solution
class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=254)
    username = models.CharField(max_length=30)
    role = models.BooleanField(default=False)