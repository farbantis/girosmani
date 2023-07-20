from django.urls import path
from rest_framework import routers
from cafe.api.resources import MenuListAPIView, OrderAPIVIewSet, OrderItemAPIVIewSet, HeaderMenuAPIView

router = routers.SimpleRouter()
router.register(r'order', OrderAPIVIewSet)
router.register(r'orderitems', OrderItemAPIVIewSet)
urlpatterns = router.urls

urlpatterns += [
    path('menu/', MenuListAPIView.as_view()),
    path('menu/<slug:group>/', MenuListAPIView.as_view()),
    path('header_menu/', HeaderMenuAPIView.as_view()),
    # path('order/', OrderAPIVIew.as_view().as_view()),
]
