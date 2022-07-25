"""
Import Modules
"""
from django.db import models

# Create your models here.
# When Django sees that we've created a new 'item' class it will
# automatically create an items table when we make and run the
# database migrations. By itself this class won't do anything
# You need to use something called class inheritance to give it some
# functionality:


class Item(models.Model):
    """
    Class Inheritance: we can inherit the base model class by putting
    models.Model. Our "item" class can now do everything the built-in
    Django model class can do.
    """
    # define the attributes that our individual items will have:

    # item_id = created automatically by Django

    # built-in Django field to indicate it will just have characters / text
    # null = false prevents items from being created without a name
    # blank = false will make the field required on forms
    # This way we're certain that a todo item can't be created without a name
    # (Python code or by a user in a web form or even an administrator in the
    # admin panel)
    # default = false ensures that the field is marked as 'not done' by default

    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        """
        To override the base Django model class naming to the same as item name
        """
        return self.name
