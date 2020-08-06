from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=50, verbose_name='Товар')
    description = models.CharField(max_length=200, null=True, blank=True, verbose_name='Описание')
    characteristic = models.TextField(null=True, blank=True, verbose_name='Характеристики')
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    image = models.ImageField("Изображение", upload_to="intstore/")
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опублековано')
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Товары'
        verbose_name = 'Товар'
        ordering = ['-published']


class Rubric(models.Model):
    name = models.CharField(max_length=40, db_index=True, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']
