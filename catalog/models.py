from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
    category = models.CharField(max_length=100, verbose_name='Категория',
                                help_text='Введите категорию продукта')
    description = models.TextField(verbose_name='Описание', **NULLABLE,
                                   help_text='Введите описание категории продукта')

    def __str__(self):
        return f'Категория: {self.category}'

    class Meta:

        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название продукта', help_text='Введите название продукта')
    description = models.TextField(verbose_name='Описание', help_text='Введите описание продукта')
    image = models.ImageField(upload_to='products/', verbose_name='Изображение', **NULLABLE,
                              help_text='Введите фото продукта. если оно есть')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория', related_name="products",
                                 help_text='Выберите категорию продукта')
    price = models.IntegerField(verbose_name='Цена', help_text='Введите цену продукта')
    created_at = models.DateField(verbose_name='Дата создания продукта',
                                  help_text='Выберите дату создания продукта')
    updated_at = models.DateField(verbose_name='Дата релиза продукта', **NULLABLE,
                                  help_text='Выберите дату релиза продукта')
    number_of_views = models.IntegerField(default=0, verbose_name='Количество просмотров')

    def __str__(self):
        return f'Наименование: {self.name}, Категория: {self.category}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def form_valid(self, form):
        pass


class Contacts(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя',
                                  help_text='Введите имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия', help_text='Введите фамилию')
    phone = models.CharField(max_length=100, verbose_name='Телефон', help_text='Введите телефон')
    message = models.CharField(max_length=100, verbose_name='Сообщение', **NULLABLE, help_text='Введите сообщение')
    email = models.EmailField(verbose_name='Электронная почта', **NULLABLE,
                              help_text='Введите адрес электронной почты')

    def __str__(self):
        return f'{self.first_name} {self.email}'

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class Version(models.Model):
    product = models.ForeignKey(Product, verbose_name='Продукт', on_delete=models.CASCADE, related_name='versions',
                                help_text='Выберите продукт')
    version_number = models.PositiveIntegerField(verbose_name='Номер версии',
                                                 help_text='Введите номер версии продукта')
    version_name = models.CharField(max_length=150, verbose_name="Название версии",
                                    help_text='Введите название версии продукта')
    version_now = models.BooleanField(default=True, verbose_name="Признак текущей версии")

    def __str__(self):
        return f" {self.version_number} | {self.version_name} "

    class Meta:
        verbose_name = "Версия"
        verbose_name_plural = "Версии"
