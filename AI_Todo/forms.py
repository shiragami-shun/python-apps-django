from django import forms
from .models import Todo, Category


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["title", "minutes", "category"]


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]
