"""
Import Modules
"""
from django.shortcuts import (
    render
    # HttpResponse
    )
from .models import Item

# Create your views here.
# def say_hello(request):
# return HttpResponse("<h1>Hello!</h1><p>This is a paragraph.</p)>"


def get_todo_list(request):
    """
    Define landing page.
    Ensure communication between the front end users and our
    database on the back end.
    Add context as a third argument to the render function to
    ensure we have access to it in our todo_list.html template.
    """
    items = Item.objects.all()  # import all items from db
    context = {  # define a dictionary with all our imported items in it
        'items': items
    }
    return render(request, "todo/todo_list.html", context)
