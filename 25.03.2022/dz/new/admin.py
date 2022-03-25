from atexit import register
from django.contrib import admin
from new.models import Customer

admin.site.register(Customer)

