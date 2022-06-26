from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.CharField(max_length=1000, blank=True, null=True)
    amount = models.IntegerField(default=1)
