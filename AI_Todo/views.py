from django.shortcuts import render
from .models import Todo
from django.shortcuts import redirect, get_object_or_404
from .forms import TodoForm, CategoryForm
from .models import Category
from openai import OpenAI
import os


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


def todo_edit(request, pk):
    todo = get_object_or_404(Todo, pk=pk)

    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect("AI_Todo")
    else:
        form = TodoForm(instance=todo)

    return render(request, "AI_Todo/todo_edit.html", {
        "form": form
    })


def todo_delete(request, pk):
    todo = get_object_or_404(Todo, id=pk)
    todo.delete()
    return redirect("AI_Todo")


client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def ai_suggest(request):
    if request.method == "POST":
        user_input = request.POST.get("request")

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You suggest short actionable todo items."
                },
                {
                    "role": "user",
                    "content": f"{user_input} からTodoを5個日本語で箇条書きで作って"
                }
            ]
        )

        result = response.choices[0].message.content

        return render(
            request,
            "AI_Todo/ai_result.html",
            {"result": result}
        )

    return render(request, "AI_Todo/ai_form.html")
