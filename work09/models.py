from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=100, verbose_name="タスク名")
    description = models.TextField(blank=True, null=True, verbose_name="詳細")
    due_date = models.DateField(verbose_name="期限日")
    is_completed = models.BooleanField(default=False, verbose_name="完了フラグ")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="登録日")

    def __str__(self):
        return self.title
