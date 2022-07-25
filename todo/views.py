"""
Import Modules
"""
from django.shortcuts import (
    render,
    # HttpResponse
    redirect
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


def add_item(request):
    """
    Define add_item.html page
    Set a variable for the name by looking up request.post.get()
    Check the post boolean data actually has a done property in it as TRUE.
    Create a ToDo item in todo_list.html
    Then redirect back to home page
    """
    if request.method == 'POST':
        name = request.POST.get('item_name')
        done = 'item_done' in request.POST
        Item.objects.create(name=name, done=done)

        return redirect('get_todo_list')
    # If its a GET request:
    return render(request, "todo/add_item.html")
