from django.shortcuts import get_object_or_404
from cafe.models import Order, Product
import json


class ContextMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            if Order.objects.filter(customer=self.request.user, is_completed=False).exists():
                existing_order = get_object_or_404(Order, customer=self.request.user, is_completed=False)
                context['order_value'] = existing_order.get_order_cost or 0
                context['order_quantity'] = existing_order.get_oder_quantity or 0
        else:
            cart = json.loads(self.request.COOKIES.get('cart', '{}'))
            context['order_value'] = sum([Product.objects.get(id=article).price * quantity for article, quantity in cart.items()])
            context['order_quantity'] = sum([pcs for pcs in cart.values()])
        return context


class CartActionsMixin:
    def get_cookie_cart_content(self):
        # cart_data = self.request.execute_script("return JSON.parse(localStorage.getItem('cart')) || {}")
        # print(f'cart data is {cart_data}')
        return json.loads(self.request.COOKIES.get('cart', '{}'))

