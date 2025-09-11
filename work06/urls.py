from django.urls import path
from . import views

urlpatterns = [
    path("", views.reiwa, name="reiwa"),
    path('', views.bmi, name='bmi'),
    path('warikan/', views.warikan, name='warikan'),
    path('savings/', views.savings, name='savings'),
    path('calculator/', views.calculator, name='calculator'),
]