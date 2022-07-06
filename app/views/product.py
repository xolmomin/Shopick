from django.views.generic import TemplateView, DetailView

from app.models import Product
from app.models import ProductImage


class ShopPage(TemplateView):
    template_name = 'app/shop.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = Product.objects.all()
        product_image = ProductImage.objects.all()

        context['products'] = product
        context['product_images']=product_image

        return context


class ShopListPage(TemplateView):
    template_name = 'app/shop-list.html'


class SingleProductPage(DetailView):
    template_name = 'app/single-product.html'
    pk_url_kwarg = 'id'
    model = Product
    context_object_name = 'product'


class ThankYouPage(TemplateView):
    template_name = 'app/thank-you.html'


class WishListPage(TemplateView):
    template_name = 'app/wishlist.html'
