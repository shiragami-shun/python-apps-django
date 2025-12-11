# recipes/forms.py
from django import forms
from .models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'ingredients', 'instructions', 'image']

        # ★ここを追加！
        labels = {
            'title': 'レシピ名',
            'ingredients': '材料',
            'instructions': '作り方',
            'image': '画像',
        }

        # 必要なら説明文も追加できる
        help_texts = {
            'title': 'レシピのタイトルを入力してください。',
            'ingredients': '材料を一行ずつ、またはカンマ区切りで入力してください。',
            'instructions': '作り方を順番に入力してください。',
            'image': '料理の写真をアップロードできます。',
        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'ingredients': forms.Textarea(
                attrs={'class': 'form-textarea', 'rows': 5}
            ),
            'instructions': forms.Textarea(
                attrs={'class': 'form-textarea', 'rows': 8}
            ),
        }

