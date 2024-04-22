from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=100, verbose_name='Категория')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)

    def __str__(self):
        return f'Категория: {self.category}'

    class Meta:

        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название продукта', help_text='Введите название продукта')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='product/foto', verbose_name='Изображение', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория', related_name="products")
    price = models.IntegerField(verbose_name='Цена')
    created_at = models.DateField(verbose_name='Дата создания продукта')
    updated_at = models.DateField(verbose_name='Дата релиза продукта', blank=True, null=True)


    def __str__(self):
        return f'Наименование: {self.name}, Категория: {self.category}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name', 'category']
