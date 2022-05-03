
from django.forms import ModelForm
from new.models import AnimalImage

class ArtForm(ModelForm):
    class Meta:
        model = AnimalImage
        fields = ['email']
    