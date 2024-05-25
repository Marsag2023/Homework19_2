import json
from django.core.management import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        with open('catalog_data.json', 'r', encoding='UTF-8') as file:
            categories = json.load(file)
            return categories

    @staticmethod
    def json_read_products():
        with open('catalog_data.json', 'r', encoding='UTF-8') as file:
            products = json.load(file)
            return products

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()
        category_for_create = []
        product_for_create = []

        for category in Command.json_read_categories():
            if category["model"] == "users.category":
                category_for_create.append(
                    Category(category=category["fields"]["category"],
                             description=category["fields"]["description"]))

        Category.objects.bulk_create(category_for_create)

        for product in Command.json_read_products():
            if product["model"] == "users.product":
                product_for_create.append(
                    Product(name=product["fields"]["name"],
                            description=product["fields"]["description"],
                            image=["fields"]["image"],
                            category=Category.objects.get(pk=product["fields"]["category"],
                            price=product["fields"]["price"],
                            created_at=product["fields"]["created_at"],
                            updated_at=product["fields"]["updated_at"])))

        Product.objects.bulk_create(product_for_create)
