from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Product, ProductImage


def home(request):
    return render( request, 'home.html' )


def product_details(request, pk):
    product = Product.objects.get(id=pk)
    # product = get_object_or_404(Product, id=pk)
    product_images = ProductImage.objects.filter(product_id=pk)
    if product:
        return render( request, 'products/Products_detail.html',
                       context={'product': product, 'product_images': product_images} )
    return render( request, 'products/Products_detail.html' )


# class ProductDetail(LoginRequiredMixin, DetailView):
#     model = Product
#     template_name = 'products/Products_detail.html'


class Shop(ListView):
    queryset = Product.objects.all()
    models = Product
    template_name = "products/shop_detail.html"


class WishList(ListView):
    model = Product
    template_name = "products/wish_list.html"


class ProductCompare(ListView):
    model = Product
    template_name = "products/product_compare.html"


class ViewCart(ListView):
    model = Product
    template_name = "products/../templates/order/view_cart.html"


class CheckOut(ListView):
    model = Product
    template_name = "products/check_out.html"


def contact_page(request):
    return render( request, 'products/contact.html' )
