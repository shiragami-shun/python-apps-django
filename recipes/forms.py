# recipes/forms.py
from django import forms
from .models import Recipe


class RecipeForm(forms.ModelForm):
    # 画像削除用のチェックボックス（追加フィールド）
    clear_image = forms.BooleanField(
        required=False,
        label="画像を削除する"
    )

    class Meta:
        model = Recipe
        fields = ['title', 'ingredients', 'instructions', 'image']  # 本来のフィールド
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'ingredients': forms.Textarea(
                attrs={'class': 'form-textarea', 'rows': 5}
            ),
            'instructions': forms.Textarea(
                attrs={'class': 'form-textarea', 'rows': 8}
            ),
        }

    def clean(self):
        cleaned_data = super().clean()
        clear = cleaned_data.get('clear_image')
        new_image = cleaned_data.get('image')

        # clear チェックが ON の場合 → 古い画像を消す
        if clear:
            cleaned_data['image'] = None

        return cleaned_data
