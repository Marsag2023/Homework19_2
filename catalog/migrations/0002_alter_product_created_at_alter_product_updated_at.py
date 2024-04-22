# Generated by Django 5.0.4 on 2024-04-22 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateField(verbose_name='Дата создания продукта'),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated_at',
            field=models.DateField(blank=True, null=True, verbose_name='Дата релиза продукта'),
        ),
    ]