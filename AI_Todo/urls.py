from django.urls import path
from . import views

urlpatterns = [
    path("", views.todo_list, name="AI_Todo"),
    path("create/", views.todo_create, name="todo_create"),
    path("category_create/", views.category_create, name="category_create"),
    path("edit/<int:pk>/", views.todo_edit, name="todo_edit"),
    path("delete/<int:pk>/", views.todo_delete, name="todo_delete")
]
