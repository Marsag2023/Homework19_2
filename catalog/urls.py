from django.urls import path
from catalog.views import ProductListView, ProductDetailView, ContactsCreateView
from catalog.apps import MainConfig

app_name = MainConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
    path('catalog/<int:pk>/', ProductDetailView.as_view(), name='view'),
    #   path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('contacts', ContactsCreateView.as_view(), name='contacts_list')
]
