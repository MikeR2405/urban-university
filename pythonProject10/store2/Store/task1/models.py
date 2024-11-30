# from django.db import models
#
# class Buyer(models.Model):
#     name = models.CharField(max_length=100)  # Имя покупателя
#     balance = models.DecimalField(max_digits=10, decimal_places=2)  # Баланс
#     age = models.IntegerField()  # Возраст
#
#     def __str__(self):
#         return self.name
#
#
# class Game(models.Model):
#     title = models.CharField(max_length=200)  # Название игры
#     cost = models.DecimalField(max_digits=10, decimal_places=2)  # Цена
#     size = models.DecimalField(max_digits=10, decimal_places=2)  # Размер файлов
#     description = models.TextField()  # Описание
#     age_limited = models.BooleanField(default=False)  # Ограничение по возрасту
#     buyers = models.ManyToManyField(Buyer, related_name='games')  # Покупатели, обладающие игрой
#
#     def __str__(self):
#         return self.title
# models.py
from django.db import models

class Buyer(models.Model):
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=200)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyers = models.ManyToManyField(Buyer, related_name='games')

    def __str__(self):
        return self.title
