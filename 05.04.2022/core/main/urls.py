from django.urls import path, include
from main.views import Mains, Lol

urlpatterns = [
    path('', Mains.as_view(), name = 'mainpage'),
    path('lol/', Lol.as_view(), name = 'otvet'),
]