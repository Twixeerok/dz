from django.contrib import admin
from main.models import Customer, book, Students



@admin.register( book)
class Boooks(admin.ModelAdmin):
    pass

@admin.register(Students)
class Stud(admin.ModelAdmin):
    fields = ('firstname', 'books')
    list_display = ('firstname', 'books')
    list_filter = ('firstname',)

@admin.register(Customer)
class Cust(admin.ModelAdmin):
    pass

