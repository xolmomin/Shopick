from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from app.models import User, City, Country, PostCode

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


