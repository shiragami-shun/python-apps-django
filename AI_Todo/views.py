from django.shortcuts import render
from .models import Todo


def todo_list(request):
    todos = Todo.objects.select_related("category").all()
    return render(request, "AI_Todo/todo_list.html", {
        "todos": todos
    })
