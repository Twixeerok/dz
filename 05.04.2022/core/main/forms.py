from turtle import title
from django.forms import ModelForm
from main.models import Customer

class ArtForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['firstname', 'lastname', 'age']
