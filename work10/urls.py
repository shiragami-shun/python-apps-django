from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('todo_home/', views.todo_home, name='todo_home'),
    path('delete/<int:todo_id>/', views.todo_delete, name='todo_delete'),
    path("edit/<int:todo_id>/", views.todo_edit, name="todo_edit"),
]
