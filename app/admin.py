from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from app.models import User, City, Country, PostCode
from app.models import Category,Product
from app.models import ProductImage

admin.site.register(User, UserAdmin)

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(PostCode)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['id', 'number']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','title',]


@admin.register(ProductImage)
class ProductIMageAdmin(admin.ModelAdmin):
    pass