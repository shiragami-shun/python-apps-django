from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Todo
from django.shortcuts import get_object_or_404
from .forms import TodoForm


# --- ログインページ ---
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("todo_home")
        else:
            return render(
                request, "work10/login.html",
                {"error": "ユーザー名またはパスワードが違います。"}
            )
    return render(request, "work10/login.html")


# --- ログアウト ---
def logout_view(request):
    logout(request)
    return redirect("login")


# --- サインアップ ---
def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            return render(
                request, 'work10/signup.html',
                {'error': 'このユーザー名はすでに使われています'}
            )
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('todo_home')
    return render(request, 'work10/signup.html')


# --- TODO一覧（ホーム） ---
def todo_home(request):
    if not request.user.is_authenticated:
        return redirect('login')

    # work10 データベースを指定
    todos = Todo.objects.using('work10').filter(user=request.user).order_by(
        '-created_at'
        )

    if request.method == 'POST':
        title = request.POST.get('title')
        due_date = request.POST.get('due_date')
        if title:
            todo = Todo(user=request.user, title=title, due_date=due_date)
            todo.save(using='work10')  # 保存先も指定
        else:
            error_message = "タスク名を入力してください"
            return render(request, "work10/todo_home.html", {
                "todos": todos, "form": None, "error_message": error_message
                })

    return render(
        request, "work10/todo_home.html", {"todos": todos, "form": None}
        )


def todo_delete(request, todo_id):
    # work10_db を明示的に指定して取得
    todo = get_object_or_404(
        Todo.objects.using('work10'), id=todo_id, user=request.user
        )
    # work10_db を指定して削除
    todo.delete(using='work10')
    return redirect('todo_home')


def todo_edit(request, todo_id):
    # work10データベースから対象Todoを取得
    todo = get_object_or_404(
        Todo.objects.using('work10'), pk=todo_id, user=request.user
        )

    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)

        if form.is_valid():
            updated_todo = form.save(commit=False)
            # ✅ チェックボックスの状態を手動で取得
            # チェックされていないときはPOSTに含まれないため、Falseにする
            updated_todo.completed = 'completed' in request.POST

            updated_todo.save(using='work10')
            return redirect('todo_home')
    else:
        form = TodoForm(instance=todo)

    return render(
        request, 'work10/todo_edit.html', {'form': form, 'todo': todo}
        )
