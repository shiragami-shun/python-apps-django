from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=200)
    estimated_minutes = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title
