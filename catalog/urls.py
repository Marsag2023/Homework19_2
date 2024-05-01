from django.urls import path
from catalog.views import product_list, product_detail, contacts

urlpatterns = [
    path('', product_list, name='product_list'),
#  path('catalog/<int:pk>/', product_detail, name='product_detail'),
    path('products/<int:pk>/', product_detail, name='product_detail'),
    path('', contacts, name='contacts')
]
