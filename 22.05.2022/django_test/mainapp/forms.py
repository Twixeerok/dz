from django.forms import ModelForm
from mainapp.models import Post

class ArtForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'price']