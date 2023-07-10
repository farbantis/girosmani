from django.urls import path
from cafe.views import Index, ProductDetailView, delivery_terms, CartView, CheckOut, payment_success, payment_fail

app_name = 'cafe'

urlpatterns = [
    path('cart/', CartView.as_view(), name='cart'),
    path('update-cart/', CartView.as_view(), name='update-cart'),
    path('cafe/checkout/', CheckOut.as_view(), name='checkout'),
    path('cafe/payment_success/', payment_success, name='payment_success'),
    path('cafe/payment_fail/', payment_fail, name='payment_fail'),
    path('product/<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('delivery_terms/', delivery_terms, name='delivery_terms'),
    path('', Index.as_view(), name='main_page'),
]
