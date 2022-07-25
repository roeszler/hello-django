"""
Import Modules
"""
from django.contrib import admin
from .models import Item  # imports the item 'model' ('Table' in SQL)

# Register your models here.
admin.site.register(Item)
