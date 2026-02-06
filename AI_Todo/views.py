from django.shortcuts import render
from .models import Todo
from django.shortcuts import redirect
from .forms import TodoForm, CategoryForm
from .models import Category


def todo_list(request):
    todos = Todo.objects.select_related("category").all()
    return render(request, "AI_Todo/todo_list.html", {
        "todos": todos
    })


def todo_create(request):
    if request.method == "POST":
        todo_form = TodoForm(request.POST)
        category_form = CategoryForm(request.POST)

        # 既存カテゴリでTodo作成
        if todo_form.is_valid():
            todo_form.save()
            return redirect("AI_Todo")

    else:
        todo_form = TodoForm()
        category_form = CategoryForm()

    return render(request, "AI_Todo/todo_form.html", {
        "todo_form": todo_form,
        "category_form": category_form
    })


def category_create(request):
    if request.method == "POST":
        name = request.POST.get("name")

        if name:
            Category.objects.create(name=name)
            return redirect("AI_Todo")

    return render(request, "AI_Todo/category_form.html")
