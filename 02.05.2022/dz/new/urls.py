from django.urls import path
from new.views import Po, Lo

urlpatterns = [
    path('cw24/', Po.as_view(), name='glav'),
    path('cw24/animal', Lo.as_view(), name='animal')
]