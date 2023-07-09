from django.urls import path
from cafe.views import Index

app_name = 'cafe'

urlpatterns = [
    path('', Index.as_view(), name='main_page'),
]
