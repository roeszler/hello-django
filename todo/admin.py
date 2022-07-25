"""
Import Modules
"""
from django.contrib import admin
from .models import Item  # imports the item 'class'

# Register your models here.
admin.site.register(Item)
