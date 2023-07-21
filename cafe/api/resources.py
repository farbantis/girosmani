from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from cafe.api.serializers import MenuListSerializer, OrderSerializer, OrderItemsSerializer, HeaderMenuSerializer
from cafe.models import Product, Order, OrderItems, Menu


class MenuListAPIView(ListAPIView):
    serializer_class = MenuListSerializer
    queryset = Product.objects.all()

    def get_queryset(self):
        qs = super(MenuListAPIView, self).get_queryset()
        group = self.kwargs.get('group')
        if group is not None:
            qs = Product.objects.filter(group__name=group)
        return qs


class HeaderMenuAPIView(ListAPIView):
    serializer_class = HeaderMenuSerializer
    queryset = Menu.objects.all()


class UserOrdersAPIView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        return super().get_queryset().filter(customer=self.request.user.id)


class OrderAPIVIewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        return super(OrderAPIVIewSet, self).get_queryset().filter(customer=self.request.user)


class OrderItemAPIVIewSet(viewsets.ModelViewSet):
    queryset = OrderItems.objects.all()
    serializer_class = OrderItemsSerializer

    def get_queryset(self):
        return super(OrderItemAPIVIewSet, self).get_queryset()\
            .filter(order__is_completed=False)\
            .filter(order__customer=self.request.user)

