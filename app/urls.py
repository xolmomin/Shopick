from django.urls import path

from views import about

urlpatterns = [
    path('about/',about,name='about'),
]