from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.core.validators import integer_validator
from django.db import models



class User(AbstractUser):
    email = models.EmailField(unique=True,max_length=255,null=True)
