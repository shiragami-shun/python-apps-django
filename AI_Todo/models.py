# AI_Todo/models.py
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Todo(models.Model):
    title = models.CharField(max_length=200)
    minutes = models.IntegerField()
    is_completed = models.BooleanField(default=False)

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title
