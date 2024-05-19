from django.contrib import admin
from catalog.models import Category, Product, Contacts, Version


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


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone', 'message', 'email', )
    list_filter = ('email',)
    search_fields = ('email',)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('id', 'version_number', 'version_name', 'product',)
    list_filter = ('product',)
    search_fields = ('version_name',)
