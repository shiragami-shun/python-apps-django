from django.db import models

class Memo(models.Model):
    # タイトル（短い文字列）
    title = models.CharField(max_length=200)

    # 本文（長文）
    content = models.TextField()

    # 作成日（自動で登録時にセットされる）
    created_at = models.DateTimeField(auto_now_add=True)

    # 更新日（更新のたびに自動で変更される）
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
