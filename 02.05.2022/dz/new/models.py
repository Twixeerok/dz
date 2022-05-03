import email
from statistics import mode
from django.db import models


class Species(models.Model):
    CHOICES = (
    ("Кот", "Кот"),
    ("Собака", "Собака"),
)

    sp = models.CharField(max_length=255,verbose_name='тип животного', choices=CHOICES)

    def __str__(self) -> str:
        return self.sp

class AnimalImage(models.Model):
    url = models.URLField(verbose_name="Адресс")
    species = models.ForeignKey(Species, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True, verbose_name="дата")
    type = models.CharField(max_length=255,verbose_name='тип')
    email = models.EmailField(verbose_name="email", blank=True)

    def __str__(self) -> str:
        return self.url