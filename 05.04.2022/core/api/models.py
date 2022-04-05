from cgitb import text
from turtle import title
from django.db import models

class State(models.Model):
    title = models.CharField(max_length=255,verbose_name='главное')
    text = models.TextField(max_length=255, verbose_name='текст')
    
    def __str__(self) -> str:
        return f'{self.title}|{self.text}'
