from django.urls import path
from new.views import get, hel, gest

urlpatterns = [
    path('', get),
    path('dz1/', gest, name = 'gets'),
    path('hello/', hel.as_view(), name = 'hello')
]