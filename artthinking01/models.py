# artthinking01/models.py
from django.db import models
from django.utils import timezone


class TimelinePost(models.Model):
    content = models.TextField(max_length=500)
    created_at = models.DateTimeField(default=timezone.now)
    author = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.author or '匿名'}: {self.content[:20]}"


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    cover_image = models.ImageField(
        upload_to='covers/', blank=True, null=True
        )  # 画像
    category = models.CharField(max_length=100, blank=True, null=True)  # カテゴリ
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'books'
        managed = False
