from pyexpat import model
from django.db import models

class book(models.Model):
    title = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return f'{self.title}'


class Students(models.Model):
    firstname = models.CharField(max_length=255)
    books = models.OneToOneField(book, null=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return f'{self.firstname}'

class Customer(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    age = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f'{self.firstname}'
