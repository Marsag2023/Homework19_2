from django.contrib import admin
from catalog.models import Category, Product


@admin.register(Product)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)
# Register your models here.


@admin.register(Category)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'category',)
    list_filter = ('category',)
    search_fields = ('category',)
