from django.shortcuts import render
from django.views.generic import TemplateView




class AboutPage(TemplateView):
    template_name = 'app/about.html'