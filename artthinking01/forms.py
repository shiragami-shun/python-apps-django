# artthinking01/forms.py
from django import forms
from .models import Book
from .models import TimelinePost


class TimelinePostForm(forms.ModelForm):
    class Meta:
        model = TimelinePost
        fields = ['content', 'author']
        widgets = {
            'content': forms.Textarea(
                attrs={'rows': 3, 'placeholder': 'ここに投稿を書いてください…'}
                ),
            'author': forms.TextInput(attrs={'placeholder': '名前（任意）'}),
        }


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'category', 'cover_image']
