from django.urls import path
from cafe.views import Index, ProductDetailView, delivery_terms

app_name = 'cafe'

urlpatterns = [
    path('product/<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('delivery_terms/', delivery_terms, name='delivery_terms'),
    path('', Index.as_view(), name='main_page'),
]
