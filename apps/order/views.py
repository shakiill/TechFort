from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from apps.products.models import Product
from .models import Cart, Order


@login_required
def add_to_cart(request, pk):
    item = get_object_or_404(Product, pk=pk)
    # current item
    order_item = Cart.objects.get_or_create(item=item, user=request.user, is_purchased=False)
    # list of orders where is_order = False /// check for already existing order
    my_orders = Order.objects.filter(user=request.user, is_order=False)
    if my_orders.exists():
        order = my_orders[0]
        if order.order_items.filter(item=item).exists():
            order_item[0].quantity += 1
            order_item.save()
            messages.info(request, "Quantity of this item is updated.")
            return redirect("products:shop")
        else:
            order.order_items.add(order_item[0])
            messages.info(request, "This item has been added to your cart.")
            return redirect("products:shop")
    else:
        order = Order(user=request.user)
        order.save()
        order.order_items.add(order_item[0])
        messages.info(request, "This item has been added to your cart.")
        return redirect("products:shop")
