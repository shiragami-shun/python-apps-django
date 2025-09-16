from django.urls import path
from . import views

urlpatterns = [
    path("omikuji/", views.omikuji, name="omikuji"),
    path("janken/", views.janken, name="janken"),
    path("hi_low/", views.hi_low, name="hi_low"),
]
