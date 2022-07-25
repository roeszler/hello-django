from django.shortcuts import (
    render
    # HttpResponse
    )

# Create your views here.
# def say_hello(request):
    # return HttpResponse("<h1>Hello!</h1><p>This is a paragraph.</p)>"
def get_todo_list(request):
    return render(request, "todo/todo_list.html")
