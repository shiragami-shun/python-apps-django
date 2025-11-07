from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("translate/", views.translate, name="translate"),
    path("translate_api/", views.translate_api, name="translate_api"),
    path("ranking/", views.ranking, name="ranking"),
    path("timeline/", views.timeline, name="timeline"),
    path("favorites/", views.favorites, name="favorites"),
    path('books/', views.book_list, name='book_list'),
    path('books/add/', views.add_book, name='add_book'),
    path('add_timeline/', views.add_timeline, name='add_timeline'),
    path('books/edit/<int:pk>/', views.edit_book, name='edit_book'),
    path('books/delete/<int:pk>/', views.delete_book, name='delete_book'),
    path('profile/', views.profile, name='profile'),
    path('books/favorite/<int:pk>/', views.favorite_book, name='favorite_book')
]
