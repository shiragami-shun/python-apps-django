from django.urls import path
from . import views

urlpatterns = [
    path("", views.todo_list, name="AI_Todo"),
    path("create/", views.todo_create, name="todo_create"),
    path("category/create/", views.category_create, name="category_create"),
]
