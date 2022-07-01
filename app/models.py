from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.core.validators import integer_validator
from django.db import models



class User(AbstractUser):
    first_name = models.CharField(max_length=255,null=True)
    last_name = models.CharField(max_length=255,null=True)
    email = models.EmailField(unique=True,max_length=255,null=True)


