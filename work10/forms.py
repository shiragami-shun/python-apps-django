from django import forms
from .models import Todo  # モデル名が Todo の場合


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        # ← ここでどのフィールドを使うか指定する
        fields = ['title', 'due_date']  # 必要に応じて他のフィールドも追加
        # もしくは全部使う場合 → fields = '__all__'
