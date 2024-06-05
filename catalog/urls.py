from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.views import ProductListView, ProductDetailView, ContactsCreateView, ProductCreateView, ProductUpdateView
from catalog.apps import MainConfig

app_name = MainConfig.name

urlpatterns = [

    path('', ProductListView.as_view(), name='list'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('catalog/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='view'),
    path('edit/<int:pk>/', ProductUpdateView.as_view(), name='edit'),
    path('contacts', ContactsCreateView.as_view(), name='contacts_list'),
]
