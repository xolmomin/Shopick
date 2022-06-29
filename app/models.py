from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.core.validators import integer_validator
from django.db import models



class User(AbstractUser):
    email = models.EmailField(unique=True,max_length=255,null=True)



class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.CharField(max_length=1000, blank=True, null=True)
    amount = models.IntegerField(default=1)
