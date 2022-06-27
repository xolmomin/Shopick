from django.urls import path

from views import  AboutPage

urlpatterns = [
    path('about/',AboutPage.as_view(),name='about'),
]