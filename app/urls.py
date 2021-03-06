from django.urls import path

from app.views.views import AboutPage, IndexPage, BlogPage, CartPage, CheckoutPage, ContactPage,SingleBlogPage
from app.views.product import  ShopPage, ShopListPage,  SingleProductPage, ThankYouPage, WishListPage


from app.views.auth import RegisterPage,LoginPage,MyAccPage
from app.views.auth import ActivateEmailView
from app.views.auth import LogoutPage, ForgotPasswordPage

urlpatterns = [
    path('', IndexPage.as_view(), name='index'),
    path('blog/', BlogPage.as_view(), name='blog'),
    path('cart/', CartPage.as_view(), name='cart'),
    path('checkout/', CheckoutPage.as_view(), name='checkout'),
    path('contact/', ContactPage.as_view(), name='contact'),
    path('about/', AboutPage.as_view(), name='about'),
    path('shop/', ShopPage.as_view(), name='shop'),
    path('shop-list/', ShopListPage.as_view(), name='shop-list'),
    path('single-blog/', SingleBlogPage.as_view(), name='single_blog'),
    path('single-product/<id>', SingleProductPage.as_view(), name='single_product'),
    path('thank-you/', ThankYouPage.as_view(), name='thank_you'),
    path('wish-list/', WishListPage.as_view(), name='wishlist'),



    path('login/', LoginPage.as_view(), name='login'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('my-account/', MyAccPage.as_view(), name='my_acc'),
    path('logout/',LogoutPage.as_view(),name='logout'),
    path('forgot/',ForgotPasswordPage.as_view(),name='forgot'),
    path('activate/<str:uuid>/<str:token>',ActivateEmailView.as_view(),name='confirm_mail')
]

# handler404 = 'app.views.error'
