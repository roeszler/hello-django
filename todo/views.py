"""
Import Modules
"""
from django.shortcuts import (
    render,
    # HttpResponse
    redirect, 
    get_object_or_404
    )
from .models import Item
from .forms import ItemForm

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
        form = ItemForm(request.POST)  # letting ItemForm's handle the data
        if form.is_valid():
            form.save()
        # name = request.POST.get('item_name')  # declaring it locally
        # done = 'item_done' in request.POST
        # Item.objects.create(name=name, done=done)
        return redirect('get_todo_list')

    form = ItemForm()  # create an instance of ItemForm() in the add_item view.
    context = {  # a context which contains the empty form.
        'form': form
    }
    # If its a GET request:
    return render(request, "todo/add_item.html", context)


def edit_item(request, item_id):
    """
    Controls the view characteristics of edit_item.html
    item_id parameter attached to the edit link
    to return template edit_item.html
    Return the item if it exists, or a 404 page not found if not.
    """
    item = get_object_or_404(Item, id=item_id)  # get a copy of the item from the db
    # create an instance of ItemForm() in the edit_item view, Telling it that it should 
    # be prefilled with the information for the item we just got from the database:

    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)  # letting ItemForm's handle the data
        if form.is_valid():
            form.save()
        return redirect('get_todo_list')
    
    form = ItemForm(instance=item)
    context = {  # a context which contains the empty form.
        'form': form
    }
    return render(request, 'todo/edit_item.html', context)  # returning i to the form


def toggle_item(request, item_id):
    """
    When a user clicks toggle, view will get the item
    Flip the status to alternately true or false and vice versa
    Redirect back to they get_todo list view
    """
    item = get_object_or_404(Item, id=item_id)  # get a copy of the item
    item.done = not item.done  # changing dome status to opposite of current status
    item.save()
    return redirect('get_todo_list')


def delete_item(request, item_id):
    """
    When a user clicks delete, this view will get the item,
    delete it and redirect back to they get_todo list view
    """
    item = get_object_or_404(Item, id=item_id)  # get a copy of the item
    item.delete()
    return redirect('get_todo_list')
