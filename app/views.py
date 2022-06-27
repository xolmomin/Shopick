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


class LoginPage(TemplateView):
    template_name = 'app/login.html'


class MyAccPage(TemplateView):
    template_name = 'app/my-account.html'


class ShopPage(TemplateView):
    template_name = 'app/shop.html'


class ShopListPage(TemplateView):
    template_name = 'app/shop-list.html'


class SingleBlogPage(TemplateView):
    template_name = 'app/single-blog.html'


class SingleProductPage(TemplateView):
    template_name = 'app/single-product.html'


class ThankYouPage(TemplateView):
    template_name = 'app/thank-you.html'


class WishListPage(TemplateView):
    template_name = 'app/wishlist.html'
