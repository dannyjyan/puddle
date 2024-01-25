from django.contrib import admin

# Register your models here.


from .models import Category, Item #.models because models.py is in same directory

admin.site.register(Category)
admin.site.register(Item)