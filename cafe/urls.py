from django.urls import path
from cafe.views import Index, ProductDetailView, delivery_terms, CartView, CheckOut

app_name = 'cafe'

urlpatterns = [
    path('cart/', CartView.as_view(), name='cart'),
    path('update-cart/', CartView.as_view(), name='update-cart'),
    path('cafe/checkout/', CheckOut.as_view(), name='checkout'),
    path('product/<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('delivery_terms/', delivery_terms, name='delivery_terms'),
    path('', Index.as_view(), name='main_page'),
]
