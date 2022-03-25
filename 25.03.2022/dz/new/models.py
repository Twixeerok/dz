from tabnanny import verbose
from django.db import models


class Customer(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    age = models.IntegerField()
    prof = models.CharField(max_length=255, verbose_name='Профссия')

    def __str__(self) -> str:
        return f'{self.firstname}|{self.age}'

    class Meta:
        verbose_name = "Пользователь"