from django.urls import path
from core.views import index, item_list, products, categories, contact

urlpatterns = [
    path('', index),
    path('cart', item_list ),
    path('products', products),
    path('categories', categories),
    path('contact', contact)
]