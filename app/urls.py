
from django.urls import path

from app.views.views import AboutPage, IndexPage, BlogPage, CartPage, CheckoutPage, ContactPage, ShopPage, ShopListPage, SingleBlogPage, SingleProductPage, ThankYouPage, WishListPage

from app.views.auth import LoginPage, MyAccPage

urlpatterns = [
    path('', IndexPage.as_view(), name='index'),
    path('blog/', BlogPage.as_view(), name='blog'),
    path('cart/', CartPage.as_view(), name='cart'),
    path('checkout/', CheckoutPage.as_view(), name='checkout'),
    path('contact/', ContactPage.as_view(), name='contact'),
    path('about/', AboutPage.as_view(), name='about'),
    path('login/', LoginPage.as_view(), name='login'),
    path('my-account/', MyAccPage.as_view(), name='my_acc'),
    path('shop/', ShopPage.as_view(), name='shop'),
    path('shop-list/', ShopListPage.as_view(), name='shop-list'),
    path('single-blog/', SingleBlogPage.as_view(), name='single_blog'),
    path('single-product/', SingleProductPage.as_view(), name='single_product'),
    path('thank-you/', ThankYouPage.as_view(), name='thank_you'),
    path('wish-list/', WishListPage.as_view(), name='wishlist'),
]

# handler404 = 'app.views.error'

