from django.urls import path
from cafe.views import Index, ProductDetailView, delivery_terms, CartView, CheckOut, payment_success, payment_fail, \
    apply_coupon, ReorderView, LocationView, OrderPDF, get_pdf_receipt

app_name = 'cafe'

urlpatterns = [
    path('cart/', CartView.as_view(), name='cart'),
    path('update-cart/', CartView.as_view(), name='update-cart'),
    path('cafe/checkout/', CheckOut.as_view(), name='checkout'),
    path('cafe/payment_success/<order_id>', payment_success, name='payment_success'),
    path('cafe/payment_fail/', payment_fail, name='payment_fail'),
    path('product/<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('delivery_terms/', delivery_terms, name='delivery_terms'),
    path('cafe/recreate-order/', ReorderView.as_view(), name='reorder'),
    path('cafe/location/', LocationView.as_view(), name='location'),
    path('cafe/apply_coupon/', apply_coupon, name='apply_coupon'),
    path('cafe/<str:group>/', Index.as_view(), name='main_page'),
    path('cafe/order/pdf/<order_id>/', get_pdf_receipt, name='order_pdf'),
    path('', Index.as_view(), name='main_page'),
]
