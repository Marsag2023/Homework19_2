# Generated by Django 5.0.4 on 2024-04-22 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_product_created_at_alter_product_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='manufactured_at',
            field=models.DateField(blank=True, max_length=20, null=True, verbose_name='Дата создания продукта'),
        ),
    ]
