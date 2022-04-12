from django.urls import path, include
from main.views import  Lol, Add

urlpatterns = [
    # path('', Mains.as_view(), name = 'mainpage'),
    path('home/', Lol.as_view(), name = 'home'),
    path('add/', Add.as_view(), name = 'add'),
]