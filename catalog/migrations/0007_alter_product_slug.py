# Generated by Django 4.2.2 on 2024-06-05 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_alter_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True, verbose_name='URL'),
        ),
    ]
