# recipes/forms.py
from django import forms
from .models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'ingredients', 'instructions', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'ingredients': forms.Textarea(
                attrs={'class': 'form-textarea', 'rows': 5}
                ),
            'instructions': forms.Textarea(
                attrs={'class': 'form-textarea', 'rows': 8}
                ),
        }
