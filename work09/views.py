from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo


# 一覧画面（Read）
def todo_list(request):
    todos = Todo.objects.using('work09').all().order_by('due_date')
    if request.method == 'POST':
        title = request.POST.get('title')
        due_date = request.POST.get('due_date')
        if title and due_date:
            Todo.objects.using('work09').create(title=title, due_date=due_date)
        return redirect('todo_list')
    return render(request, 'work09/todo_list.html', {'todos': todos})


# 作成画面（Create）→ 今回は一覧ページにフォームがあるので個別画面は省略可
def todo_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        due_date = request.POST.get('due_date')
        Todo.objects.create(title=title, due_date=due_date)
        return redirect('todo_list')
    return render(request, 'work09/todo_create.html')


# 編集画面（Update）
def todo_edit(request, pk):
    todo = get_object_or_404(Todo.objects.using('work09'), pk=pk)
    if request.method == 'POST':
        if 'update' in request.POST:
            todo.title = request.POST.get('title')
            todo.due_date = request.POST.get('due_date')
            todo.is_completed = 'is_completed' in request.POST
            todo.save(using='work09')
            return redirect('todo_list')
        elif 'delete' in request.POST:
            todo.delete(using='work09')
            return redirect('todo_list')
    return render(request, 'work09/todo_edit.html', {'todo': todo})


# 削除処理（Delete）※ボタン経由で呼ばれる
def todo_delete(request, pk):
    todo = get_object_or_404(Todo.objects.using('work09'), pk=pk)
    todo.delete(using='work09')
    return redirect('todo_list')