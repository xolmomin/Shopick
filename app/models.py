from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.core.validators import integer_validator, MaxValueValidator, MinValueValidator
from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


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


class Category(MPTTModel):
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    name = models.CharField(max_length=60, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField()
    discount = models.IntegerField(validators=[
        MaxValueValidator(70, message='It cannot higer 70 percent'),
        MinValueValidator(20, message='It cannot exceed 20 percent')
    ])
    category = models.ForeignKey('app.Category', on_delete=models.CASCADE)
    description = models.CharField(max_length=300)

    @property
    def images(self):
        return self.products_images.all()

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    product = models.ForeignKey('app.Product', on_delete=models.CASCADE, related_name="products_images")
    image = models.ImageField(upload_to='product-images/')

    def __str__(self):
        return self.product.title
