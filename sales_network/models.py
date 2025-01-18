from django.db import models
from django.urls import reverse

class Supplier(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя поставщика')
    debt = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name='Задолжность')

    def get_absolute_url(self):
        return reverse('admin:sales_network_supplier_change', args=[self.id])

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название продукта')
    model = models.CharField(max_length=255, verbose_name='модель')
    release_date = models.DateField(verbose_name='Дата выхода на рынок')


class Node(models.Model):
    LEVEL_CHOICES = [
        (0, 'Завод'),
        (1, 'Розничная сеть'),
        (2, 'Индивидуальный предприниматель'),
    ]

    name = models.CharField(max_length=255, verbose_name='Название')
    email = models.EmailField(verbose_name='Почта')
    country = models.CharField(max_length=100, verbose_name='Страна')
    city = models.CharField(max_length=100, verbose_name='Город')
    street = models.CharField(max_length=100, verbose_name='Улица')
    house_number = models.CharField(max_length=25, verbose_name='Номер дома')
    products = models.ManyToManyField(Product, verbose_name='Продукты')
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name='Поставщик')
    debt = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name='Задолжность')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    level = models.IntegerField(choices=LEVEL_CHOICES, verbose_name='Уровень Иерархии')

    def __str__(self):
        return self.name
