from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.home, name='home' ),
    # path('home/', views.home, name='home'),
    # path('shop/', views.shop, name='shop'),
    path('shop/', views.Shop.as_view(), name='shop' ),
    path('product/<pk>', views.product_details, name='productDetails' ),
    path('wishlist/', views.WishList.as_view(), name='wishlist' ),
    path('compare/', views.ProductCompare.as_view(), name='compare' ),
    path('cart/', views.ViewCart.as_view(), name='cart' ),
    path('checkout/', views.CheckOut.as_view(), name='checkout' ),
    path('contact/', views.contact_page, name='contact' ),

]