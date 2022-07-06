from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.core.validators import integer_validator, MaxValueValidator
from django.db import models


class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True, null=True)
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    email = models.EmailField(unique=True, max_length=255, null=True)
    office_addres = models.CharField(max_length=255, blank=True, null=True)
    city = models.ForeignKey('app.City', on_delete=models.CASCADE, null=True, blank=True)
    country = models.ForeignKey('app.Country', on_delete=models.CASCADE, null=True, blank=True)
    post_code = models.ForeignKey('app.PostCode', on_delete=models.CASCADE, null=True, blank=True)
    number = models.CharField(max_length=25, validators=[integer_validator], null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)


class BaseModel(models.Model):
    time_updated = models.DateTimeField(auto_now=True)
    time_created = models.DateTimeField(auto_now_add=True)


class Country(BaseModel):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class City(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class PostCode(BaseModel):
    number = models.IntegerField(validators=[MaxValueValidator(8)])
    description = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.number
