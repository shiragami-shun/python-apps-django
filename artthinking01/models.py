# artthinking01/models.py
from django.db import models
from django.utils import timezone
from django.shortcuts import render


class TimelinePost(models.Model):
    content = models.TextField(max_length=500)
    created_at = models.DateTimeField(default=timezone.now)
    author = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.author or '匿名'}: {self.content[:20]}"


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=100, default='未分類')
    description = models.TextField(blank=True, null=True)
    cover_image = models.ImageField(upload_to='covers/', blank=True, null=True)
    favorites = models.IntegerField(default=0)  # ← お気に入りカウント

    def __str__(self):
        return self.title


def book_list(request):
    books = Book.objects.using('artthinking01').all()
    return render(request, 'artthinking01/book_list.html', {'books': books})


class Post(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}『{self.title}』"
