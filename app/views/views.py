from django.shortcuts import render
from django.views.generic import TemplateView


class IndexPage(TemplateView):
    template_name = 'app/index.html'


class BlogPage(TemplateView):
    template_name = 'app/blog.html'


class CartPage(TemplateView):
    template_name = 'app/cart.html'


class CheckoutPage(TemplateView):
    template_name = 'app/checkout.html'


class ContactPage(TemplateView):
    template_name = 'app/contact.html'


class AboutPage(TemplateView):
    template_name = 'app/about.html'

class SingleBlogPage(TemplateView):
    template_name = 'app/single-blog.html'




# def error(request,exception):
#     return render(request,'app/404.html')
